
File("/etc/redis.conf",
    owner = "root",
    group = "root",
    mode = 0644,
    content = Template("redis/redis.conf.j2"))
