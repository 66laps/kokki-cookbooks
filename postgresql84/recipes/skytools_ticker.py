
from kokki import *

include_recipe("postgresql84.skytools")

File("/etc/skytools/ticker.ini",
    owner = "root",
    content = Template("postgresql84/skytools-ticker.ini.j2"))
