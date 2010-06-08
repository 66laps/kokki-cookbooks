
import os
from kokki import *

include_recipe("mongodb")
include_recipe("supervisor")

cookbooks.supervisor.SupervisorService("avatartare")

Package("python-pycurl")

# Clone project
Directory(os.path.dirname(env.avatatare.path), mode=0755)
Execute("git clone git://github.com/samuel/avatartare.git %s" % env.avatatare.path,
    creates = env.avatatare.path,
)

# Bootstrap the environment
Execute("avatartare-bootstrap",
    command = "python bin/bootstrap.py env",
    cwd = env.avatatare.path,
    creates = "%s/env" % env.avatatare.path,
)

# Config
File("avatartare-local_settings.py",
    path = "%s/local_settings.py" % env.avatatare.path,
    content = Template("avatartare/local_settings.py.j2"),
    notifies = [("restart", env.resources["SupervisorService"]["avatartare"])])

# Setup Supervisor to start and monitor the processes
File("%s/supervisor.d/avatartare" % env.supervisor.config_path,
    content = Template("lefora/supervisor-avatartare.j2"),
    notifies = [("restart", env.resources["SupervisorService"]["avatartare"])])
