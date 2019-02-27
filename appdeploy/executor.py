import logging
import paramiko

def ssh_command(ssh, host, cmd):
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode('utf-8')
    err = stderr.read().decode('utf-8')

    if out:
        logging.info("============== OUTPUT ========================")
        logging.info("host:["+host+"] Command:"+cmd)
        logging.info(out)
        logging.info("==============================================")
    if err:
        logging.error("============= ERROR =========================")
        logging.error("host:["+host+"] Command:"+cmd)
        logging.error(err)
        logging.error("=============================================")

def sftp(ssh, file):
    sftp = ssh.open_sftp()

    try:
        sftp.stat(file["path"])
    except FileNotFoundError:
        sftp.mkdir(file["path"])

    sftp.put(file["local"], file["path"]+file["name"])
    sftp.chmod(file["path"]+file["name"], int(file["chmod"]))
    sftp.close()
    ssh.close()

def ssh_connect(host, user, password, cmd):

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)

        if type(cmd) is dict:
            #Is a file
            sftp(ssh, cmd)
        else:
            #Is a command
            ssh_command(ssh, host, cmd)

    except Exception as e:
        print('Connection Failed')
        print(e)

def proc(hosts, cmd_list):
    logging.debug("EXEC")
    logging.debug(hosts)
    logging.debug(cmd_list)
    for c in cmd_list:
        for h in hosts:
            logging.debug("executing command on "+ str(h))
            ssh_connect(h["name"], h["user"], h["password"], c)
