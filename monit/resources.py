
__all__ = ["MonitService"]

from pluto import *

class MonitService(Service):
    provider = "pluto.cookbooks.monit.MonitServiceProvider"

    supports_restart = BooleanArgument(default=True)
    supports_status = BooleanArgument(default=True)
    supports_reload = BooleanArgument(default=False)
