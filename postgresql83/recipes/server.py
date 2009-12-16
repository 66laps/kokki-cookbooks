
import os
from pluto import *

Package("postgresql",
    package_name = "postgresql-8.3")

Service("postgresql",
    service_name = "postgresql-8.3",
    supports_restart = True,
    supports_reload = True,
    supports_status = True)

File("pg_hba.conf",
    owner = "postgres",
    group = "postgres",
    mode = 0600,
    path = os.path.join(env.postgresql.config_dir, "pg_hba.conf"),
    content = Template("postgresql83/pg_hba.conf.j2"),
    notifies = [("reload", env.resources["Service"]["postgresql"])])

File("postgresql.conf",
    owner = "postgres",
    group = "postgres",
    mode = 0600,
    path = os.path.join(env.postgresql.config_dir, "postgresql.conf"),
    content = Template("postgresql83/postgresql.conf.j2"),
    notifies = [("restart", env.resources["Service"]["postgresql"])])
