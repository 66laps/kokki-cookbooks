# Martin Galpin (m@66laps.com)

from kokki import *

from kokki.cookbooks.s3cmd.utils import s3cfg_path_for_user

Package("s3cmd")

File("creating s3cfg",
    path = s3cfg_path_for_user(env.s3cmd.user),
    content = Template("s3cmd/s3cfg.j2"),
    owner = env.s3cmd.user,
    group = env.s3cmd.group if env.s3cmd.group is not None else env.s3cmd.user,
    mode = 0644)