
from subprocess import Popen, STDOUT, PIPE
from pluto import *

def setup():
    p = Popen("locale -a", shell=True, stdout=PIPE)
    out = p.communicate()[0]
    env.locales = out.strip().split("\n")
    env.postgresql84.locale = env.locales[0]
    for l in env.locales:
        if 'utf8' in l.lower() or 'utf-8' in l.lower():
            env.postgresql84.locale = l
            break

setup()
