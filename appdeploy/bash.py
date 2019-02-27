SUDO="sudo %s"
UPDATE="apt-get update -y"
INSTALL="apt-get install %s -y"
UNINSTALL="apt-get remove %s -y"
CHOWN="chown %s:%s %s"
UNAME='uname --all'

def setup(env):
    list=[]
    if env["dependencies"]["uninstall"]:
        for p in env["dependencies"]["uninstall"]:
          list.append(SUDO % (UNINSTALL % p))

    if env["dependencies"]["install"]:
        for p in env["dependencies"]["install"]:
          list.append(SUDO % (INSTALL % p))
    return list

def deploy(env):
    if env["files"]:
        list = []
        for f in env["files"]:
            list.append(f)
            list.append(SUDO % str(CHOWN % (f["owner"],f["group"],str(f["path"]+f["name"]))))
    return list

def stop(env):
    s = (SUDO % env["service"]["stop"])
    return [s]

def start(env):
    s = (SUDO % env["service"]["start"])
    return [s]

def restart(env):
    list=[]
    list = list+stop(env)
    list = list+start(env)
    return list

def update(env):
    return [SUDO % UPDATE]

def uname(env):
    return [SUDO % UNAME]

cmds = {'setup' : setup, 'deploy' : deploy, 'stop' : stop, 'start' : start, 'restart' : restart, 'update': update, 'uname': uname}
