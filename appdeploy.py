#!/usr/bin/env python
import argparse
from appdeploy.slk_engine import AppDeploy
import logging
from logging.config import fileConfig
import sys
sys.setrecursionlimit(50000)

def main(args):
    logging.getLogger("paramiko").setLevel(logging.INFO)

    logger = logging.getLogger()
    logger.setLevel(args.log_level)
    logging.debug("started")

    logger.debug('Input file is: '+args.file.name)
    logger.debug('Action is: '+args.action)

    s_deploy = SlackDeploy(args.file.name, args.action)
    s_deploy.process()
    logging.debug("Process finished")

if __name__ == "__main__":
    actions=["setup", "deploy", "stop", "start", "restart"]
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', "--action", choices=['setup', 'deploy', 'start', 'stop', 'restart', 'update', 'uname'], required=True)
    parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True)
    parser.add_argument('-d', '--debug', action='store_const', dest='log_level', const=logging.DEBUG, default=logging.INFO)
    args = parser.parse_args()
    main(args)
