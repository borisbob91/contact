#! usr/bin/env python3
#coding: utf-8

import os
import sys
import pathlib

File_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(File_PATH)



def configure():
    import os

    script_dir = BASE_DIR

    absolute_dependencies = [
        f"{script_dir}/interface",
        f"{script_dir}/interface/pop",
        f"{script_dir}/images",
    ]

    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    return {}