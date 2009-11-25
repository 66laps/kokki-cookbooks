
include_recipe("monit")

from monit import monitrc

def install_package(name, url, creates):
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
            "./configure && make install\n") % dict(url=url, dirname=dirname, filename=filename)
    )

install_package("gearmand",
    creates = "/usr/local/sbin/gearmand",
    url = "http://launchpad.net/gearmand/trunk/0.10/+download/gearmand-0.10.tar.gz")

Package("libevent-dev")
Directory("/var/run/gearmand",
    owner = "nobody",
    mode = 0755)
monitrc("gearmand",
    content = Template("gearmand/monit.conf.j2"))
