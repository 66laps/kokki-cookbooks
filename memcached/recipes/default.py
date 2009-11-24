
from pluto import *

Package("memcached", action="upgrade")
Package("libmemcache-dev", action="upgrade")
Service("memcached")

File("/etc/memcached.conf",
    content = Template(
        "memcached/templates/memcached.conf.j2",
        variables = dict(
            memory = env.attr['memcached']['memory'],
            user = env.attr['memcached']['user'],
            port = env.attr['memcached']['port'],
            ipaddress = env.attr.get('ipaddress', '127.0.0.1'),
        )),
    owner = "root",
    group = "root",
    mode = 0644,
    notifies = [("restart", Resource.lookup("Service", "memcached"), True)])
