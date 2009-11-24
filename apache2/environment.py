
# Where the various parts of apache are
if env.system.platform in ('redhat', 'centos', 'fedora', 'suse'):
    env['apache']['dir']     = "/etc/httpd"
    env['apache']['log_dir'] = "/var/log/httpd"
    env['apache']['user']    = "apache"
    env['apache']['binary']  = "/usr/sbin/httpd"
    env['apache']['icondir'] = "/var/www/icons/"
elif env.system.platform in ("debian", "ubuntu"):
    env['apache']['dir']     = "/etc/apache2"
    env['apache']['log_dir'] = "/var/log/apache2"
    env['apache']['user']    = "www-data"
    env['apache']['binary']  = "/usr/sbin/apache2"
    env['apache']['icondir'] = "/usr/share/apache2/icons"
else:
    env['apache']['dir']     = "/etc/apache2"
    env['apache']['log_dir'] = "/var/log/apache2"
    env['apache']['user']    = "www-data"
    env['apache']['binary']  = "/usr/sbin/apache2"
    env['apache']['icondir'] = "/usr/share/apache2/icons"
