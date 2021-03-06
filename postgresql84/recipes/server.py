
import os
from kokki import *

Service("postgresql",
    service_name = "postgresql-8.4",
    supports_restart = True,
    supports_reload = True,
    supports_status = True,
    action = "nothing")

Package("postgresql",
    package_name = "postgresql-8.4",
    notifies = [("stop", env.resources["Service"]["postgresql"], True)])

File("pg_hba.conf",
    owner = "postgres",
    group = "postgres",
    mode = 0600,
    path = os.path.join(env.postgresql84.config_dir, "pg_hba.conf"),
    content = Template("postgresql84/pg_hba.conf.j2"),
    notifies = [("reload", env.resources["Service"]["postgresql"])])

File("postgresql.conf",
    owner = "postgres",
    group = "postgres",
    mode = 0600,
    path = os.path.join(env.postgresql84.config_dir, "postgresql.conf"),
    content = Template("postgresql84/postgresql.conf.j2"),
    notifies = [("restart", env.resources["Service"]["postgresql"])])
