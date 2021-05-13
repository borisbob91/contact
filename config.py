#! usr/bin/env python3
#coding: utf-8

import os
import sys

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DB_ROOT = os.path.join(BASE_DIR, 'models')
DATA_ROOT = os.path.join(BASE_DIR, 'data')
UID_ROOT = os.path.join(BASE_DIR, 'uid')
db_root = 'models/contact.db'

""" Vcard contact file format configuration
to get more data, complete list like:
    VCARD_FORMAT = ['TEL;CELL', 'N', 'FN', ['PHOTO', 'ADDR']]
 """
VCARD_FORMAT = [ 'N', 'FN', 'TEL;CELL']
vcard_VERSION = 2.1
DELIMITER = ['BEGIN:VCARD', 'END:VCARD']

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