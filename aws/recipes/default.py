
from pluto import *

Package("python-boto")

Package("xfsprogs")

for vol in env.aws.volumes:
    cookbooks.aws.EBSVolume(vol['volume_id'],
        availability_zone = env.aws.availability_zone,
        device = vol['device'],
        action = "attach")

    if vol.get('fstype'):
        Execute("mkfs.%(fstype)s %(device)s" % vol)
            not_if = """if [ "`file -s %(device)s`" = "%(device)s: data" ]; then exit 1; fi""" % vol)

    if vol.get('mount_point'):
        Mount(vol['mount_point'],
            device = vol['device'],
            fstype = vol.get('fstype'),
            options = vol.get('fsoptions', ["noatime"]),
            action = ["mount", "enable"])
