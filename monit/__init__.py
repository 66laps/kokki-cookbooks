
from pluto import *

def monitrc(name, content):
    return File("monitrc-%s" % name,
        content = content,
        owner = "root",
        group = "root",
        mode = 0644,
        path = "%s/monit.d/%s" % (env['monit']['config_path'], name),
        notifies = [("restart", Resource.lookup("Service", "monit"))])
