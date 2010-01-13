
from kokki import *

Package("monit")

File("%s/monitrc" % env['monit']['config_path'],
    owner = "root",
    group = "root",
    mode = 0700,
    content = Template("monit/monitrc.j2"))

if env.system.platform == "ubuntu":
    File("/etc/default/monit",
        content = Template("monit/default.j2"))

Directory("%s/monit.d" % env['monit']['config_path'],
    owner = "root",
    group = "root",
    mode = 0700)

Directory("/var/monit",
    owner = "root",
    group = "root",
    mode = 0700)

Service("monit",
    supports_restart = True,
    subscribes = [('restart', env.resources['File']["%s/monitrc" % env['monit']['config_path']])])
