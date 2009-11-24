
from pluto import *

Package("memcached", action="upgrade")
Package("libmemcache-dev", action="upgrade")
Service("memcached")

File("/etc/memcached.conf",
    content = Template(
        "memcached/templates/memcached.conf.j2",
        variables = dict(
            memory = env['memcached']['memory'],
            user = env['memcached']['user'],
            port = env['memcached']['port'],
            ipaddress = env.get('ipaddress', '127.0.0.1'),
        )),
    owner = "root",
    group = "root",
    mode = 0644,
    notifies = [("restart", Resource.lookup("Service", "memcached"), True)])
