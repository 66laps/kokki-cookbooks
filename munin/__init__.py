
from kokki import *


# def munin_plugin(name, install=True):
#             present: {
#                 $file = $plugin ? { '' => $name, default => $plugin }
#               file { "/etc/munin/plugins/$name":
#                   ensure  => link,
#                   target  => "/usr/share/munin/plugins/$file",
#                   notify  => Service["munin-node"],
#               }
#             }
#             absent: {
#                 file { "/etc/munin/plugins/$name":
#                     ensure => absent,
#                   notify  => Service["munin-node"],
