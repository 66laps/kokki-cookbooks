
from pluto import *

def nginx_site(name, enable=True):
    import os
    if enable:
        Execute("nxensite %s" % name,
            command = "/usr/sbin/nxensite %s" % name,
            notifies = [("reload", env.resources["Service"]["nginx"])],
            not_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env['nginx']['dir'], name)))
    else:
        Execute("nxdissite %s" % name,
            command = "/usr/sbin/nxdissite %s" % name,
            notifies = [("reload", env.resources["Service"]["nginx"])],
            only_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env['nginx']['dir'], name)))
