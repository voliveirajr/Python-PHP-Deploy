# Python-PHP-Deploy

It is Python Exercise for an assignment challenge, the aim is manage debian nodes using Paramiko implementation of the SSHv2 protocol not utilising our of shelf tools as ansible, puppet, etc.
This is limited to manage packages, move files to the server, restart web server.

## Python version

  It was implemented and tested using Python **3.7.2**:

  This should be executed in an environment (virtualenv) using the `requirements.txt` file

## TL;DR

run:

```
$ python appdeploy.py -f production/production.yaml -a setup
$ python appdeploy.py -f production/production.yaml -a deploy
$ python appdeploy.py -f production/production.yaml -a restart
```

## Project Structure

`/slack`            : source code
`/production`       : environment descriptor and files
`slackdeploy.py`    : main file


## Command Line Interface

usage: `slackdeploy.py [-h] -a {setup,deploy,start,stop,restart,update,uname} -f FILE [-d]`

 - a: defines an Action
    * setup: Install and Uninstall debian packages listed in descriptor file
    * deploy: Upload files listed in descriptor file
    * update: update all packages (apt-get update)
    * uname: performs uname command on nodes
    * restart: restart the web server accordingly with defined on descriptor file

 - f: Yaml descriptor file path

 - d: Debug loggin

## Descriptor File
The descriptor file is a yaml file where nodes, credentials, files and webserver are defined.
You can find in this file:

Hosts: list of hosts defining address, user and password

Dependencies: Defines the deb packages, it has 2 sub items, Install and Uninstall, this gonna perform `apt-get install` and `apt-get remove` respectively.

Files: What files should be uploaded, remote path, permissions, user and group.

# Author

**Volmar Oliveira Junior**
 
volmar.oliveira.jr@gmail.com
