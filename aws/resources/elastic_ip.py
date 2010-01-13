
from kokki import *

class ElasticIP(Resource):
    actions = ["associate", "disassociate"]

    aws_access_key = ResourceArgument()
    aws_secret_access_key = ResourceArgument()
    ip = ResourceArgument()
    timeout = ResourceArgument(default=3*60) # None or 0 for no timeout
