import os
import random
import string
import util


def create():
    letters = string.ascii_letters
    digits = string.digits
    with open(''.join(random.choice(letters + digits) for i in range(8)), 'w') as f:
        print ('created')


def delete(filepath):
    try:
        os.remove(filepath)
    except OSError as e:
        print ("Error during delete" + e.message)


def readfile(filepath):
    if os.path.exists(filepath):
        with open(filepath) as f:
            return f.read()
    else:
        print ("file doesn't exists")


def metadata(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            return {'path': os.path.abspath(filename),
                    'create_date': util.convert_date(filename),
                    'modification_time': util.convert_date(filename),
                    'size': os.path.getsize(filename)}
    else:
        print ("file doesn't exist")


def mkdirp(path):
    if not os.path.exists(path):
        os.mkdir(path, 0750)
