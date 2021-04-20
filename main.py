import argparse

import config
import filemanager
import util

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-command", type=str)
    parser.add_argument("-filename", type=str, dest="filename")
    arguments = parser.parse_args()

    commands = {"create", "delete", "read", "metadata"}
    current_command = arguments.command
    if current_command not in commands:
        print ("command not found")
        exit()

    working_dir = config.WORKING_DIR
    filemanager.mkdirp(working_dir)

    filename = arguments.filename
    if current_command == "create":
        filemanager.create()
    if current_command == "delete":
        filemanager.delete(util.create_abspath(filename, working_dir))
    if current_command == "read":
        print(filemanager.readfile(util.create_abspath(filename, working_dir)))
    if current_command == "metadata":
        print filemanager.metadata(util.create_abspath(filename, working_dir))
