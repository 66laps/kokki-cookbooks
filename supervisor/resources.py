
from pluto import *

class SupervisorService(Service):
    provider = "supervisor.providers.SupervisorServiceProvider"

    supports_restart = BooleanArgument(default=True)
    supports_status = BooleanArgument(default=True)
    supports_reload = BooleanArgument(default=False)
