
__all__ = ["MonitService"]

from kokki import *

class MonitService(Service):
    provider = "kokki.cookbooks.monit.MonitServiceProvider"

    supports_restart = BooleanArgument(default=True)
    supports_status = BooleanArgument(default=True)
    supports_reload = BooleanArgument(default=False)
