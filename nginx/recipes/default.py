
from pluto import *

Package("nginx")

Directory(env.attr['nginx']['log_dir'],
    mode = 0755,
    owner = env.attr['nginx']['user'],
    action = 'create')

for nxscript in ('nxensite', 'nxdissite'):
    File("/usr/sbin/%s" % nxscript,
        content = Template("nginx/templates/%s.j2" % nxscript),
        mode = 0755,
        owner = "root",
        group = "root")

File("nginx.conf",
    path = "%s/nginx.conf" % env.attr['nginx']['dir'],
    content = Template("nginx/templates/nginx.conf.j2"),
    owner = "root",
    group = "root",
    mode = 0644)

File("%s/sites-available/default" % env.attr['nginx']['dir'],
    content = Template("nginx/templates/default-site.j2"),
    owner = "root",
    group = "root",
    mode = 0644)

Service("nginx",
    supports_status = True,
    supports_restart = True,
    supports_reload = True,
    action = "start",
    subscribes = [("reload", Resource.lookup("File", "nginx.conf"))])
