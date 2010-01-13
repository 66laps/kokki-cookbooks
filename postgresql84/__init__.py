
from subprocess import Popen, STDOUT, PIPE
from kokki import *

def setup():
    postgresql_locale = env.system.locales[0]
    for l in env.system.locales:
        if 'utf8' in l.lower() or 'utf-8' in l.lower():
            postgresql_locale = l
            break
    env.set_attributes({
        'postgresql84.locale': postgresql_locale,
    })

setup()
