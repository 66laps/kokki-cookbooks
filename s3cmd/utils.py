from kokki import Fail, env

def s3cfg_path_for_user(user):
    if env.system.os == "linux":
        if user == "root":
            return "/root/.s3cfg"
        return "/home/%s/.s3cfg" % user
    elif env.system.platform == "mac_os_x":
        return "/Users/%s/.s3cfg" % user
    raise Fail("Unable to determine s3cfg path for user %s on os %s platform %s" % (user, env.system.os, env.system.platform))