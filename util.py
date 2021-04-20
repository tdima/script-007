import os
import datetime


def create_abspath(filename, working_dir):
    if filename == "" or working_dir == "":
        print ("specify filename or working directory")
        exit()
    return os.path.join(working_dir, filename)


def convert_date(filename):
    date = datetime.date
    return date.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')