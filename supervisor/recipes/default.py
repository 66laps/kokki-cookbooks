
from monit import monitrc

include_recipe("monit")

Package("supervisor",
    provider = "pluto.providers.package.easy_install.EasyInstallProvider")

File("supervisord.conf",
    path = "%s/supervisord.conf" % env.supervisor.config_path,
    content = Template("supervisor/supervisord.conf.j2"))

Directory("supervisor.d",
    path = "%s/supervisor.d" % env.supervisor.config_path)

monitrc("supervisord",
    content = Template("supervisor/monit.conf.j2"))
