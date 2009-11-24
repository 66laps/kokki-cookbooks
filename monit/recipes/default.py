
from pluto import *

Package("monit")

File("%s/monitrc" % env.attr['monit']['config_path'],
    owner = "root",
    group = "root",
    mode = 0700,
    content = Template("monit/templates/monitrc.j2"))

if env.system.platform == "ubuntu":
    File("/etc/default/monit",
        content = Template("monit/templates/default.j2"))

Directory("%s/monit.d" % env.attr['monit']['config_path'],
    owner = "root",
    group = "root",
    mode = 0700)

Directory("/var/monit",
    owner = "root",
    group = "root",
    mode = 0700)

Service("monit",
    supports_restart = True,
    subscribes = [('restart', Resource.lookup('File', "%s/monitrc" % env.attr['monit']['config_path']))])
