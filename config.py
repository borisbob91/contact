#! usr/bin/env python3
#coding: utf-8

import os
import sys
import pathlib

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
DATA_DIR = os.path.join(BASE_DIR, 'data')
SIMPLRE_DIR = os.path.join(DATA_DIR, 'simples')
SIMPLRE_INPUTS = os.path.join(SIMPLRE_DIR, 'inputs')
OUTPOUTS_DIR = os.path.join(SIMPLRE_DIR, 'outputs')


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