
import os
from kokki import *

include_recipe("mongodb")
include_recipe("supervisor")

cookbooks.supervisor.SupervisorService("avatartare")

Package("python-pycurl")

# Clone project
Directory(os.path.dirname(env.avatartare.path), mode=0755)
Execute("git clone git://github.com/samuel/avatartare.git %s" % env.avatartare.path,
    creates = env.avatatare.path,
)

# Bootstrap the environment
Execute("avatartare-bootstrap",
    command = "python bin/bootstrap.py env",
    cwd = env.avatartare.path,
    creates = "%s/env" % env.avatartare.path,
)

# Config
File("avatartare-local_settings.py",
    path = "%s/local_settings.py" % env.avatartare.path,
    content = Template("avatartare/local_settings.py.j2"),
    notifies = [("restart", env.resources["SupervisorService"]["avatartare"])])

# Setup Supervisor to start and monitor the processes
File("%s/supervisor.d/avatartare" % env.supervisor.config_path,
    content = Template("avatartare/supervisor.j2"),
    notifies = [("restart", env.resources["SupervisorService"]["avatartare"])])
