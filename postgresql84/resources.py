__all__ = ["PostgreSQLUser", "PostgreSQLDatabase"]

from kokki import *

# Basic PostgreSQL management commands - Martin Galpin (m@66laps.com)
# Inspired by the Chef recipes at https://github.com/findsyou/cookbooks/
class PostgreSQLUser(Resource):
    '''
    Defines a PostgreSQL user with an optional password.

    The available privileges (as booleans) are:
        superuser, createdb, inherit and login.
    '''
    provider = "kokki.cookbooks.postgresql84.PostgreSQLUserProvider"

    action = ForcedListArgument(default="include")
    username = ResourceArgument()
    password = ResourceArgument()
    privileges = ResourceArgument(default={})
    actions = Resource.actions + ["include", "exclude"]

    def validate(self):
        if not self.username:
            raise Fail("At least a username is required.")

class PostgreSQLDatabase(Resource):
    '''
    Defines a PostgreSQL database with an optional owner.
    '''
    provider = "kokki.cookbooks.postgresql84.PostgreSQLDatabaseProvider"

    action = ForcedListArgument(default="include")
    database = ResourceArgument()
    owner = ResourceArgument(default='postgres')

    actions = Resource.actions + ["include", "exclude"]

    def validate(self):
        if not self.database:
            raise Fail("At least a database name is required.")