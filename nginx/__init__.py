
from pluto import *

def nginx_site(name, enable=True):
    import os
    if enable:
        Execute("nxensite %s" % name,
            command = "/usr/sbin/nxensite %s" % name,
            notifies = [("reload", Resource.lookup("Service", "nginx"))],
            not_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env.attr['nginx']['dir'], name)))
    else:
        Execute("nxdissite %s" % name,
            command = "/usr/sbin/nxdissite %s" % name,
            notifies = [("reload", Resource.lookup("Service", "nginx"))],
            only_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env.attr['nginx']['dir'], name)))

def setup_environment(env):
    if env.system.platform in ("debian", "ubuntu"):
        env.attr['nginx']['dir']     = "/etc/nginx"
        env.attr['nginx']['log_dir'] = "/var/log/nginx"
        env.attr['nginx']['user']    = "www-data"
        env.attr['nginx']['binary']  = "/usr/sbin/nginx"
    else:
        env.attr['nginx']['dir']     = "/etc/nginx"
        env.attr['nginx']['log_dir'] = "/var/log/nginx"
        env.attr['nginx']['user']    = "www-data"
        env.attr['nginx']['binary']  = "/usr/sbin/nginx"
