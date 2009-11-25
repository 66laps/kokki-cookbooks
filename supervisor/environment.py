if env.system.platform == "ubuntu":
    env.supervisor.binary_path = "/usr/local/bin"
else:
    env.supervisor.binary_path = "/usr/bin"
