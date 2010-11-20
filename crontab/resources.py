# Martin Galpin (m@66laps.com)

__all__ = ["CronJob"]

from kokki import *

class CronJob(Resource):
    '''
    Defines a system wide cron job.
    '''
    provider = "kokki.cookbooks.crontab.CronJobProvider"

    action = ForcedListArgument(default="enable")
    minute = ResourceArgument(default='*')
    hour = ResourceArgument(default='*')
    day_of_month = ResourceArgument(default='*')
    month = ResourceArgument(default='*')
    day_of_week = ResourceArgument(default='*')
    user = ResourceArgument(default='root')
    command = ResourceArgument()

    actions = Resource.actions + ["enable", "disable"]

    def validate(self):
        if not self.command:
            raise Fail("A command is required.")
