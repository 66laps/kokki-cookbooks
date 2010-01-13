
from kokki import *

Package("nginx")

Directory(env.nginx.log_dir,
    mode = 0755,
    owner = env.nginx.user,
    action = 'create')

for nxscript in ('nxensite', 'nxdissite'):
    File("/usr/sbin/%s" % nxscript,
        content = Template("nginx/%s.j2" % nxscript),
        mode = 0755,
        owner = "root",
        group = "root")

File("nginx.conf",
    path = "%s/nginx.conf" % env.nginx.dir,
    content = Template("nginx/nginx.conf.j2"),
    owner = "root",
    group = "root",
    mode = 0644)

File("%s/sites-available/default" % env.nginx.dir,
    content = Template("nginx/default-site.j2"),
    owner = "root",
    group = "root",
    mode = 0644)

Service("nginx",
    supports_status = True,
    supports_restart = True,
    supports_reload = True,
    action = "start",
    subscribes = [("reload", env.resources["File"]["nginx.conf"])])
