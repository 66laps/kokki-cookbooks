
from subprocess import Popen, STDOUT, PIPE
from pluto import *

def setup():
    p = Popen("locale -a", shell=True, stdout=PIPE)
    out = p.communicate()[0]
    env.locales = out.strip().split("\n")
    postgresql_locale = env.locales[0]
    for l in env.locales:
        if 'utf8' in l.lower() or 'utf-8' in l.lower():
            postgresql_locale = l
            break
    env.set_attributes({
        'postgresql84.locale': postgresql84.locale,
    })

setup()
