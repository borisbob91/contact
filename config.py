#! usr/bin/env python3
#coding: utf-8

import os
import sys

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DB_ROOT = os.path.join(BASE_DIR, 'models')
UID_ROOT = os.path.join(BASE_DIR, 'uid')
db_root = 'models/contact.db'


def configure():

    script_dir = BASE_DIR

    absolute_dependencies = [
        f"{script_dir}/interface",
        f"{script_dir}/interface/pop",
        f"{script_dir}/images",
        f"{script_dir}/models",
    ]

    from myutils import set_syspath
    set_syspath(absolute_dependencies)


    return {}
    

if __name__ == '__main__':

    configure()