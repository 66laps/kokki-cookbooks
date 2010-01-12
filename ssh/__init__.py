
from pluto import *
from pluto.cookbooks.ssh.providers import SSHKnownHostProvider
from pluto.cookbooks.ssh.resources import SSHKnownHost

def SSHConfig(name, hosts, mode=0600, **kwargs):
    File(name,
        mode = mode,
        content = Template("ssh/config.j2", {'hosts': hosts}),
        **kwargs)
