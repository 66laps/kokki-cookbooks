# Martin Galpin (m@66laps.com)

__all__ = ["CronJobProvider"]

import re

from kokki import *

CRONTAB_PATH = "/etc/crontab"

class CronJobProvider(Provider):
    def action_enable(self):
        entry = self._get_entry()
        existing = self._get_crontabs()
        if entry not in existing:
            self._append_crontab(entry)
            self.resource.updated()

    def action_disable(self):
        entry = self._get_entry()
        existing = self._get_crontabs()
        if entry in existing:
            # rewrite the file without this line
            # TODO this feels dangerous.
            with open(CRONTAB_PATH, 'w') as f:
                for e in existing:
                    if e != entry:
                        e = e if isinstance(e, str) else self._to_string(e)
                        f.write('%s\n' % e)
            self.resource.updated()

    def _get_entry(self):
        return {
            'cron': [self.resource.minute, self.resource.hour,
                     self.resource.day_of_month, self.resource.month,
                     self.resource.day_of_week, self.resource.user],
            'command': self.resource.command
        }

    def _get_crontabs(self):
        with open(CRONTAB_PATH) as f:
            lines = f.readlines()
        # crude matching of crontab jobs
        # ignores comment lines, environment variables and newlines
        # creates a list of lines in the where each cron entry is replaced
        # with a dictionary. this makes it trivial to remove entries and
        # write out a new file.
        for index, line in enumerate(lines):
            if not re.match('^#|(.+=)|\n', line):
                job = line.replace('\t', ' ').strip().split(' ')
                # magic number - six crontab columns
                lines[index] = {'cron': job[:6], 'command': ' '.join(job[6:])}
        return lines

    def _append_crontab(self, entry):
        with open(CRONTAB_PATH, 'a+') as f:
            f.write('%s\n' % self._to_string(entry))

    def _to_string(self, entry):
        return ' '.join(entry['cron'] + [entry['command']])

