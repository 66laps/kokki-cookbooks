
from monit import monitrc

version = "1.02"
dirname = "redis-%s" % version
filename = "%s.tar.gz" % dirname
url = "http://redis.googlecode.com/files/%s" % filename

Script("install-redis",
    not_if = lambda:os.path.exists("/usr/local/bin/redis-server"),
    cwd = "/usr/local/src",
    code = (
        "wget %(url)s\n"
        "tar -zxvf %(filename)s\n"
        "cd %(dirname)s\n"
        "make install\n"
        "cp redis-server /usr/local/sbin\n"
        "cp redis-cli redis-benchmark /usr/local/bin\n") % dict(url=url, dirname=dirname, filename=filename)
    )

install_package("redis",
    configure = False,
    creates = "/usr/local/bin/redis-server",
    url = "http://redis.googlecode.com/files/redis-1.02.tar.gz")

File("redis.conf",
    path = env.redis.configfile,
    owner = "root",
    group = "root",
    mode = 0644,
    content = Template("redis/redis.conf.j2"))
monitrc("redis",
    content = Template("redis/monit.conf.j2"))
