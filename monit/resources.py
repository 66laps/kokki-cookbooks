
from pluto import *

class MonitService(Service):
    provider = "monit.providers.MonitServiceProvider"

    supports_restart = BooleanArgument(default=True)
    supports_status = BooleanArgument(default=True)
    supports_reload = BooleanArgument(default=False)
