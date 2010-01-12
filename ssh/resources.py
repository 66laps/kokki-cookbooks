
__all__ = ["SSHKnownHost"]

import os.path
from pluto import *
from pluto.cookbooks.ssh.utils import ssh_path_for_user

class SSHKnownHost(Resource):
    provider = "pluto.cookbooks.ssh.SSHKnownHostProvider"

    action = ForcedListArgument(default="include")
    host = ResourceArgument(default=lambda obj:obj.name)
    keytype = ResourceArgument()
    key = ResourceArgument()
    hashed = BooleanArgument(default=True)
    user = ResourceArgument()
    path = ResourceArgument()

    actions = Resource.actions + ["include", "exclude"]

    def validate(self):
        if not self.path:
            if not self.user:
                raise Fail("Either sshpath or user is requires for SSHKnownHost")
            self.path = os.path.join(ssh_path_for_user(self.user), "known_hosts")
