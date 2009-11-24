
import os
from pluto import *

def apache2_conf(name):
    File("%s/mods-available/%s.conf" % (env['apache']['dir'], name),
        content = Template('apache2/templates/mods/%s.conf.j2' % name),
        notifies = [("restart", Resource.lookup("Service", "apache2"))])

def apache2_module(name, enable=True, conf=False):
    if conf:
        apache2_conf(name)

    if enable:
        Execute("a2enmod %s" % name,
            command = "/usr/sbin/a2enmod %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            not_if = lambda:os.path.exists("%s/mods-enabled/%s.load" % (env['apache']['dir'], name)))
    else:
        Execute("a2dismod %s" % name,
            command = "/usr/sbin/a2dismod %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            only_if = lambda:os.path.exists("%s/mods-enabled/%s.load" % (env['apache']['dir'], name)))

def apache2_site(name, enable=True):
    if enable:
        Execute("a2ensite %s" % name,
            command = "/usr/sbin/a2ensite %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            not_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env['apache']['dir'], name)),
            only_if = lambda:os.path.exists("%s/sites-available/%s" % (env['apache']['dir'], name)))
    else:
        Execute("a2dissite %s" % name,
            command = "/usr/sbin/a2dissite %s" % name,
            notifies = [("restart", Resource.lookup("Service", "apache2"))],
            only_if = lambda:os.path.exists("%s/sites-enabled/%s" % (env['apache']['dir'], name)))
