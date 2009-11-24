
from pluto import *

Package("munin-node")

File("munin-node.conf",
    path = "/etc/munin/munin-node.conf",
    owner = "root",
    group = "root",
    mode = 0644,
    content = Template("munin/templates/munin-node.conf.j2"))

Service("munin-node",
    subscribes = [("restart", Resource.lookup("File", "munin-node.conf"))])
