
from pluto import *
from monit import monitrc

include_recipe("monit")

Package("supervisor",
    provider = "pluto.providers.package.easy_install.EasyInstallProvider")

monitrc("supervisord",
    content = Template("supervisord/templates/monit.conf.j2"))
