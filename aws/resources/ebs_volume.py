
from kokki import *

class EBSVolume(Resource):
    provider = "kokki.cookbooks.aws.EBSVolumeProvider"

    actions = ["create", "attach", "detach", "snapshot"]

    volume_id = ResourceArgument(default=lambda obj:obj.name)
    aws_access_key = ResourceArgument()
    aws_secret_access_key = ResourceArgument()
    size = ResourceArgument()
    snapshot_id = ResourceArgument()
    availability_zone = ResourceArgument()
    device = ResourceArgument()
    timeout = ResourceArgument(default=3*60) # None or 0 for no timeout
