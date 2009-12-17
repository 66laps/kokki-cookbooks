
from pluto import *

class EBSVolume(Resource):
    provider = "pluto.cookbooks.aws.EBSVolumeProvider"

    actions = ["create", "attach", "detach", "snapshot"]

    aws_access_key = ResourceArgument()
    aws_secret_access_key = ResourceArgument()
    size = ResourceArgument()
    snapshot_id = ResourceArgument()
    availability_zone = ResourceArgument()
    device = ResourceArgument()
    volume_id = ResourceArgument()
    timeout = ResourceArgument(default=3*60) # None or 0 for no timeout
