
import hashlib
import hmac
from base64 import b64decode, b64encode
from pluto import Fail, env

class SSHKnownHostsFile(object):
    def __init__(self, path=None):
        self.hosts = []
        self.parse(path)

    def parse(self, path):
        self.hosts = []
        with open(path, "r") as fp:
            for line in fp:
                line = line.strip()
                if not line:
                    continue

                addr, keytype, key = line.split(' ')
                if addr.startswith('|1|'):
                    # Hashed host entry
                    salt, hosthash = addr.split('|')[2:]
                    self.hosts.append((1, b64decode(salt), b64decode(hosthash), keytype, key))
                else:
                    # Unhashed
                    for a in addr.split(','):
                        self.hosts.append((0, a, keytype, key))

    def save(self, path):
        with open(path, "w") as fp:
            fp.write(str(self))

    def includes(self, host):
        host = host.lower()
        for h in self.hosts:
            if h[0] == 0:
                if h[1] == host:
                    return True
            elif h[0] == 1:
                hosthash = self.hash(host, h[1])[0]
                if hosthash == h[2]:
                    return  True
        return False

    def hash(self, host, salt=None):
        if not salt:
            salt = self.generate_salt()
        return hmac.new(salt, host, digestmod=hashlib.sha1).digest(), salt

    def generate_salt(self):
        return os.urandom(20)

    def add_host(self, host, keytype, key, hashed=True, verify=True):
        host = host.lower()
        if verify and self.includes(host):
            return False

        if hashed:
            hosthash, salt = self.hash(host)
            self.hosts.append((1, salt, hosthash, keytype, key))
        else:
            self.hosts.append((0, host, keytype, key))

        return True

    def remove_host(self, host):
        host = host.lower()
        new_hosts = []
        for h in self.hosts:
            if h[0] == 0:
                if h[1] == host:
                    continue
            elif h[0] == 1:
                hosthash = self.hash(host, h[1])[0]
                if hosthash == h[2]:
                    continue
            new_hosts.append(h)

        found = len(new_hosts) != len(self.hosts)
        self.hosts = new_hosts
        return found

    def __str__(self):
        out = []
        unhashed = {} # Group unhashed hosts by the key
        for h in self.hosts:
            if h[0] == 0:
                k = (h[2], h[3])
                if k not in unhashed:
                    unhashed[k] = [h[1]]
                else:
                    unhashed[k].append(h[1])
            elif h[0] == 1:
                out.append("|1|%s|%s %s %s" % (b64encode(h[1]), b64encode(h[2]), h[3], h[4]))
        for k, host in unhashed.items():
            out.append("%s %s %s" % (",".join(host), k[0], k[1]))
        out.append("\n")
        return "\n".join(out)
def ssh_path_for_user(user):
    if env.system.platform == "linux":
        if user == "root":
            return "/root/.ssh/"
        return "/home/%s/" % user
    elif env.system.platform == "mac_os_x":
        return "/Users/%s/.ssh/" % user
    raise Fail("Unable to determine ssh path for user %s on platform %s" % (user, env.system.platform))
