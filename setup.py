
import os
import sys
import subprocess as sp
import json

class Config:
    FILE = "config.json"
    RPI_IP_ADDR = "rpi-ip-addr"
    RPI_USER = "rpi-user"
    TARGET_FOLDER = "target-folder"
    REQUIRED_FILES = "required-files"

class Install:
    '''Performs install operations for segway code'''

    def __init__(self):
        '''Established configuration data'''

        # Get current directory
        self.cwd = os.getcwd()

        # Check if config file is present
        if not os.path.exists(self.cwd + "/" + Config.FILE):
            self.make_config()

        self.config = json.load(open(Config.FILE))

    def make_config(self):
        '''Generate a configuration file'''

        config = open(Config.FILE, "w")
        ip_addr = raw_input("Enter your RPi Ipv4 address: ")
        user = raw_input("Enter the userame of your RPi account: ")
        folder = raw_input("Enter the RPi target folder ~/: ")
        required_files = ["accl_test.py", "pid.py"]

        data = {
            Config.RPI_IP_ADDR: ip_addr,
            Config.RPI_USER: user,
            Config.REQUIRED_FILES: required_files,
            Config.TARGET_FOLDER: folder
        }

        config.write(json.dumps(data, indent=4, sort_keys=True))
        config.close()

    def run(self):
        '''Copies files to target machine'''

        for file in self.config[Config.REQUIRED_FILES]:
            command = "scp "
            command += self.cwd + "/" + file + " "
            command += self.config[Config.RPI_USER] + "@" + self.config[Config.RPI_IP_ADDR] + ":~/" + self.config[Config.TARGET_FOLDER] + "/"
            shell_cmd = sp.Popen(command, shell=True)
            shell_cmd.communicate()


if __name__ == "__main__":
    install = Install()
    install.run()