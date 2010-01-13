
__all__ = ["SupervisorService"]

from kokki import *

class SupervisorService(Service):
    provider = "kokki.cookbooks.supervisor.SupervisorServiceProvider"

    supports_restart = BooleanArgument(default=True)
    supports_status = BooleanArgument(default=True)
    supports_reload = BooleanArgument(default=False)
