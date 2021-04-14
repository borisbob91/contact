
from interface.tkinker_import import *


from interface.app_gui import  MainApp

def main():
    app = tkinter.Tk()
    window = MainApp(app)
    app.mainloop()

if __name__ == '__main__':
    
    main()