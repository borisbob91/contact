#! usr/bin/env python3
#coding: utf-8

import config

from interface.login_gui import login_gui_launcher
from interface import main_laucnher
from models import db_config


if __name__ == '__main__':
        
    config = config.configure()

    db = db_config.configure()

    login_gui_launcher()
    #main_laucnher()