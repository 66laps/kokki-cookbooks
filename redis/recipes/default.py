
from monit import monitrc

def install_package(name, url, creates, configure=True):
    import os
    filename = url.rsplit('/', 1)[-1]
    dirname = filename
    while dirname.rsplit('.', 1)[-1] in ('gz', 'tar', 'tgz', 'bz2'):
        dirname = dirname.rsplit('.', 1)[0]

    if not dirname:
        raise Fail("Enable to figure out directory name of project for URL %s" % url)

    Script("install-%s" % name,
        not_if = lambda:os.path.exists(creates),
        cwd = "/usr/local/src",
        code = (
            "wget %(url)s\n"
            "tar -zxvf %(filename)s\n"
            "cd %(dirname)s\n"
            "%(configure)smake install\n") % dict(url=url, dirname=dirname, filename=filename, configure="./configure && " if configure else "")
    )

install_package("redis",
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
