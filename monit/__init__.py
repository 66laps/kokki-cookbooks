
from pluto import *
from pluto.cookbooks.monit.providers import *
from pluto.cookbooks.monit.resources import *

def monitrc(name, content):
    return File("monitrc-%s" % name,
        content = content,
        owner = "root",
        group = "root",
        mode = 0644,
        path = "%s/monit.d/%s" % (env['monit']['config_path'], name),
        notifies = [("restart", env.resources["Service"]["monit"])])

def setup():
    env.set_attributes({
            'monit.config_path': "/etc/monit",
        }, overwrite=True)

setup()
