
import urllib2
from pluto import *
from pluto.cookbooks.aws.providers import EBSVolumeProvider
from pluto.cookbooks.aws.resources import EBSVolume

def get_ec2_metadata(key):
    res = urllib2.urlopen("http://169.254.169.254/2008-02-01/meta-data/" + key)
    return res.read().strip()

def setup():
    env.set_attributes({
        'aws.instance_id': get_ec2_metadata('instance-id'),
        'aws.instance_type': get_ec2_metadata('instance-type'),
        'aws.availability_zone': get_ec2_metadata('placement/availability-zone'),
    }, overwrite=True)

setup()
