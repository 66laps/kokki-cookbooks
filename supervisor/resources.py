
__all__ = ["SupervisorService"]

from pluto import *

class SupervisorService(Service):
    provider = "pluto.cookbooks.supervisor.SupervisorServiceProvider"

    supports_restart = BooleanArgument(default=True)
    supports_status = BooleanArgument(default=True)
    supports_reload = BooleanArgument(default=False)
