
from pluto import *
from monit import monitrc

def install_package(name, url):
    from pluto import *
    filename = url.rsplit('/', 1)[-1]
    name = filename.split('.')[0]
    Execute("(cd /usr/local/src ; wget %s ; tar -zxvf %s ; cd %s ; ./configure ; make install)" % (url, filename, name))

install_package("gearmand", url="http://launchpad.net/gearmand/trunk/0.10/+download/gearmand-0.10.tar.gz")

Package("libevent-dev")
Directory("/var/run/gearmand",
    owner = "nobody",
    mode = 0755)
monitrc("gearmand",
    content = Template("gearmand/monit.conf.j2"))
