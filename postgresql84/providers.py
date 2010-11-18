__all__ = ["PostgreSQLUserProvider", "PostgreSQLDatabaseProvider"]

import subprocess

from kokki import *

def _success(cmd):
    return not subprocess.call(cmd, shell=True)

# TODO Replace with Kokki user/group attribute when main branch hits release
def _pgcmd(cmd):
    return "sudo -u postgres %s" % cmd

# Basic PostgreSQL management commands - Martin Galpin (m@66laps.com)
# Inspired by the Chef recipes at https://github.com/findsyou/cookbooks/
class PostgreSQLUserProvider(Provider):
    def action_include(self):
        # Create role update SQL
        defaults = {
                'superuser': False, 'createdb': False,
                'createrole': False, 'inherit': True,
                'login': True,
            }
        defaults.update(self.resource.privileges)
        sql_privileges = ['%s%s' % ('' if defaults[p] else 'NO', p.upper()) for p in defaults.keys()]

        sql = "ROLE %s %s" % (self.resource.username, ' '.join(sql_privileges))
        if self.resource.password is not None:
            sql = "%s WITH PASSWORD '%s'" % (sql)

        # Check if a given user already exists
        exists_cmd = "psql -c 'SELECT usename FROM pg_catalog.pg_user' " \
            "| grep '^ %s$'" % self.resource.username

        # Update existing user if it already exists
        Execute('alter postgresql84 user %s' % self.resource.username,
            command=_pgcmd('psql -c "ALTER %s"' % sql),
            only_if=lambda:_success(_pgcmd(exists_cmd)))

        # Create a new user if it doesn't already exist
        Execute('creating postgresql84 user %s' % self.resource.username,
            command=_pgcmd('psql -c "CREATE %s"' % sql),
            not_if=lambda:_success(_pgcmd(exists_cmd)))

        self.resource.updated()

    def action_exclude(self):
        # Check if a given user already exists
        exists_cmd = "psql -c 'SELECT usename FROM pg_catalog.pg_user' " \
            "| grep '^ %s$'" % self.resource.username

        sql = 'DROP ROLE IF EXISTS %s' % self.resource.username
        Execute('drop postgresql84 user %s' % self.resource.username,
            command=_pgcmd('psql -c "%s"' % sql),
            only_if=lambda:_success(exists_cmd))

        self.resource.updated()

class PostgreSQLDatabaseProvider(Provider):
    def action_include(self):
        # Check if a given database already exists
        exists_cmd = "psql -f /dev/null %s" % self.resource.database

        # Update database owner if it already exists
        Execute('updating postgresql84 database owner for %s' % self.resource.database,
            command=_pgcmd("psql -c 'ALTER DATABASE %s OWNER TO %s'"
                % (self.resource.database, self.resource.owner)),
            only_if=lambda:_success(_pgcmd(exists_cmd)))

        # Else, create a new database
        Execute('creating postgresql84 database %s' % self.resource.database,
            command=_pgcmd('createdb %s' % self.resource.database),
            not_if=lambda:_success(_pgcmd(exists_cmd)))

        self.resource.updated()

    def action_exclude(self):
        # Check if a given database already exists
        exists_cmd = "psql -f /dev/null %s" % self.resource.database

        Execute('dropping postgresql84 database "%s" if it exists' % self.resource.database,
            command=_pgcmd("psql -c 'DROP DATABASE IF EXISTS %s" % self.resource.database),
            only_if=lambda:_success(_pgcmd(exists_cmd)))

        self.resource.updated()