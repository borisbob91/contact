#! usr/bin/env python3
#coding: utf-8

import config

from interface.tkinker_import import *

from interface import  tkinker_import

from interface.interface import  Interface

def main():
    app = tkinter.Tk()
    window = Interface(app)
    app.mainloop()

if __name__ == '__main__':
    config = config.configure()
    main()