#! usr/bin/env python3
#coding: utf-8

import config

from interface.tkinker_import import *

from interface import  tkinker_import

from interface.interface import  Interface

from interface.login_gui import login_gui_launcher



if __name__ == '__main__':
    config = config.configure()
    login_gui_launcher()

