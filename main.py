#! usr/bin/env python3
# coding: utf-8
# import config
""" Main APP
Here is the main module to launche the application
"""


from interface.login_gui import login_gui_launcher
from interface import main_launcher
from models import db_config
from models.models import  CheckSuperUser
from session_data import read_token
import config
import logging
import  time

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    config = config.configure()
    with  open('main.txt', "a") as files:
        files.write(f'last lauched : {time.strftime("%Y-%d-%m-%H:%M:%I") }  - {logger} \n')
    db = db_config.configure()
    a = read_token()
    auto_login = CheckSuperUser.init(a.u_id, a.u_name, a.u_pdw)
    if auto_login:
        main_launcher()
    else:
        login_gui_launcher()
    # main_launcher()
