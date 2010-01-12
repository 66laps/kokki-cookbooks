
__all__ = ["SSHKnownHostProvider"]

import os
import re
import subprocess
from pluto import *
from pluto.cookbooks.ssh.utils import SSHKnownHostsFile

class SSHKnownHostProvider(Provider):
    def action_include(self):
        hosts = SSHKnownHostsFile(self.resource.path)
        modified = False
        for host in self.resource.host.split(','):
            if hosts.add_host(host, self.resource.keytype, self.resource.key, hashed=self.resource.hashed):
                modified = True
                self.log.info("[%s] Added host %s to known_hosts file %s" % (self, host, self.resource.path))
            else:
                self.log.debug("[%s] Host %s already in known_hosts file %s" % (self, host, self.resource.path))
        if modified:
            hosts.save(self.resource.path)
            self.resource.updated()

    def action_exclude(self):
        hosts = SSHKnownHostsFile(self.resource.path)
        modified = False
        for host in self.resource.host.split(','):
            if hosts.remove_host(host):
                modified = True
                self.log.info("[%s] Removed host %s to known_hosts file %s" % (self, host, self.resource.path))
            else:
                self.log.debug("[%s] Host %s not found in known_hosts file %s" % (self, host, self.resource.path))
        if modified:
            hosts.save(self.resource.path)
            self.resource.updated()
