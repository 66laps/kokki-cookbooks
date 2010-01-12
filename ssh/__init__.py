
from pluto import *
from pluto.cookbooks.ssh.providers import SSHKnownHostProvider, SSHAuthorizedKeyProvider
from pluto.cookbooks.ssh.resources import SSHKnownHost, SSHAuthorizedKey

def SSHConfig(name, hosts, mode=0600, **kwargs):
    File(name,
        mode = mode,
        content = Template("ssh/config.j2", {'hosts': hosts}),
        **kwargs)
