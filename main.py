#! usr/bin/env python3
#coding: utf-8

import config

from interface.login_gui import login_gui_launcher
from interface import main_laucnher
from models import db_config


if __name__ == '__main__':
    try:
        db = open(f'{config.BASE_DIR}/{config.db_root}', 'r')
        db.close()
    except FileNotFoundError:
        db_config.create_repertoire_table()
        db_config.create_user_table()
        
    config = config.configure()
    #login_gui_launcher()
    main_laucnher()

