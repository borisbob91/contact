#! usr/bin/env python3
# coding:utf-8

from interface.tkinker_import import *




class AbooutGui:
    _app_widht  = 912
    _app_height = 663

    def  __init__(self, top):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        sub_window_x = AbooutGui._app_widht // 2
        sub_window_y = AbooutGui._app_height // 2

        _screen_x = int(top.winfo_screenwidth())
        _screen_y = int(top.winfo_screenheight())

        _posi_x = (AbooutGui._app_widht // 2) - (sub_window_x // 2)
        _posi_y = (AbooutGui._app_height // 2) - (sub_window_y // 2)
        
        top.title('Apropos de l\'auteur ')
        top.geometry(f"{sub_window_x}x{sub_window_y}+{sub_window_x}+{sub_window_y}")
        top.resizable(False, False)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.127, height=15, width=169)
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(font="-family {gothic} -size 12")
        self.Label1.configure(text='''Auteur: Boris Bob''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.066, rely=0.333, height=15, width=99)
        self.Label1_1.configure(activebackground="#f9f9f9")

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.037, rely=0.252, height=25, width=259)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(font="-family {gothic} -size 12")
        self.Label1_2.configure(text='''Email: borisbob91@gmail.com''')

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.024, rely=0.418, height=15, width=169)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(font="-family {gothic} -size 12")
        self.Label1_3.configure(text='''Version: 1.5.0''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.048, rely=0.555, height=15, width=369)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(font="-family {gothic} -size 12")
        self.Label1_4.configure(text='''Dépot: gitlab/bgkinjecteursqli/contact.git''')

        self.Label1_5 = tk.Label(top)
        self.Label1_5.place(relx=0.05, rely=0.697, height=15, width=189)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(font="-family {gothic} -size 12")
        self.Label1_5.configure(text='''Pays: Côte d'ivoire''')

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.044, rely=0.836, height=15, width=169)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(font="-family {gothic} -size 12")
        self.Label1_6.configure(text='''Licence: Gratuit''')


def about_gui_launcher():
    global top
    top = tk.Toplevel()
    windows = AbooutGui(top)
    top.mainloop()

def about_gui_destroy():
    top.destroy()

if __name__ == '__main__':
    about_gui_launcher()