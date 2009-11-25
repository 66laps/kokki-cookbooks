
from monit import monitrc

include_recipe("monit")

Package("supervisor",
    provider = "pluto.providers.package.easy_install.EasyInstallProvider")

monitrc("supervisord",
    content = Template("supervisor/monit.conf.j2"))
