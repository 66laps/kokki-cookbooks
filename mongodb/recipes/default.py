
import os
from contextlib import closing
from kokki import *

apt_list_path = '/etc/apt/sources.list.d/mongodb.list'

if not os.path.exists(apt_list_path):
    apt = None
    if env.system.platform == "ubuntu":
        ver = env.system.lsb['release']
        if ver == '10.04':
            apt = 'deb http://downloads.mongodb.org/distros/ubuntu 10.4 10'
        elif ver == '9.10':
            apt = 'deb http://downloads.mongodb.org/distros/ubuntu 9.10 10gen'
        elif ver == '9.04':
            apt = 'deb http://downloads.mongodb.org/distros/ubuntu 9.4 10gen'
    elif env.system.platform == "debian":
        ver = env.system.lsb['release']
        if ver == '5.0':
            apt = 'deb http://downloads.mongodb.org/distros/debian 5.0 10gen'

    if not apt:
        raise Fail("Can't find a mongodb package for your platform/version")

    with closing(open(apt_list_path, 'w')) as fp:
        fp.write(apt + "\n")

    import subprocess
    subprocess.call("apt-get update", shell=True)

Package("mongodb-stable")

Service("mongodb")
File("/etc/mongodb.conf",
    owner = "root",
    group = "root",
    mode = 0644,
    content = Template("mongodb/mongodb.conf.j2"),
    notifies = [("restart", env.resources["Service"]["mongodb"])])
