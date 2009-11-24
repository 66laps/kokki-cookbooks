
import os
from pluto import *

def apache2_conf(name):
    File("%s/mods-available/%s.conf" % (env.attr['apache']['dir'], name),
        content = Template('apache2/templates/mods/%s.conf.j2' % name),
        notifies = [("restart", Resource.lookup("Service", "apache2"))])

def apache2_module(name, enable=True, conf=False):
    if conf:
        apache2_conf(name)

    if enable:
        Execute("a2enmod %s" % name,
            command = "/usr/sbin/a2enmod %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            not_if = lambda:os.path.exists("%s/mods-enabled/%s.load" % (env.attr['apache']['dir'], name)))
    else:
        Execute("a2dismod %s" % name,
            command = "/usr/sbin/a2dismod %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            only_if = lambda:os.path.exists("%s/mods-enabled/%s.load" % (env.attr['apache']['dir'], name)))

def apache2_site(name, enable=True):
    if enable:
        Execute("a2ensite %s" % name,
            command = "/usr/sbin/a2ensite %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            not_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env.attr['apache']['dir'], name)),
            only_if = lambda:os.path.exists("%s/sites-available/%s" % (env.attr['apache']['dir'], name)))
    else:
        Execute("a2dissite %s" % name,
            command = "/usr/sbin/a2dissite %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            only_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env.attr['apache']['dir'], name)))

def setup_environment(env):
    # Where the various parts of apache are
    if env.system.platform in ('redhat', 'centos', 'fedora', 'suse'):
        env.attr['apache']['dir']     = "/etc/httpd"
        env.attr['apache']['log_dir'] = "/var/log/httpd"
        env.attr['apache']['user']    = "apache"
        env.attr['apache']['binary']  = "/usr/sbin/httpd"
        env.attr['apache']['icondir'] = "/var/www/icons/"
    elif env.system.platform in ("debian", "ubuntu"):
        env.attr['apache']['dir']     = "/etc/apache2"
        env.attr['apache']['log_dir'] = "/var/log/apache2"
        env.attr['apache']['user']    = "www-data"
        env.attr['apache']['binary']  = "/usr/sbin/apache2"
        env.attr['apache']['icondir'] = "/usr/share/apache2/icons"
    else:
        env.attr['apache']['dir']     = "/etc/apache2"
        env.attr['apache']['log_dir'] = "/var/log/apache2"
        env.attr['apache']['user']    = "www-data"
        env.attr['apache']['binary']  = "/usr/sbin/apache2"
        env.attr['apache']['icondir'] = "/usr/share/apache2/icons"
