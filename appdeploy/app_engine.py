import logging
import yaml
import io
import appdeploy.bash as bash
import appdeploy.executor as e

class AppDeploy(object):
    def __init__(self, file, action):
        self.file = file
        self.action = action

    def process(self):
        logging.info("Starting Process")

        # Read YAML file
        with open(self.file, 'r') as stream:
            environment = yaml.load(stream)
            logging.debug(environment)

        #build command list based on action
        cmd_list = bash.cmds[self.action].__call__(environment)
        logging.debug(cmd_list)

        logging.debug("start executor")
        e.proc(environment["hosts"], cmd_list)
