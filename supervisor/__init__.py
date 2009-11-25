
from pluto import *

def supervisor_config(name, content):
    return File("supervisor-%s" % name,
        content = content,
        owner = "root",
        group = "root",
        mode = 0644,
        path = "%s/supervisor.d/%s" % (env.supervisor.config_path, name),
        notifies = [("reload", env.resources["Service"]["supervisor"])])
