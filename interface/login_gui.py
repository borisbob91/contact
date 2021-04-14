#! usr/bin/env python3
# coding: utf-8

from .tkinker_import import *
from .support import *

from .tooltip import ToolTip

from interface.interface import main_laucnher
from interface.message_box import show_warming, show_yes_no

class LoginSignup:
    _password = ''
    _username = ''
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+401+226")
        top.minsize(1, 1)
        top.maxsize(1585, 870)
        top.resizable(1,  1)
        top.title("Identification")
        top.configure(background="#82d8c1")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.483, rely=0.067, relheight=0.744
                , relwidth=0.5)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {gothic} -size 14")
        self.Labelframe1.configure(text='''Connexion''')
        self.Labelframe1.configure(background="#82d8c1")

        self.username_label = tk.Label(self.Labelframe1)
        self.username_label.place(relx=0.07, rely=0.101, height=40, width=182
                , bordermode='ignore')
        self.username_label.configure(activebackground="#f9f9f9")
        self.username_label.configure(background="#82d8c1")
        self.username_label.configure(font="-family {gothic} -size 14")
        self.username_label.configure(foreground="#fff")
        self.username_label.configure(relief="groove")
        self.username_label.configure(text='''Utilisateur''')

        self.username_entry = tk.Entry(self.Labelframe1)
        self.username_entry.place(relx=0.067, rely=0.218, height=37
                , relwidth=0.753, bordermode='ignore')
        self.username_entry.configure(background="white")
        self.username_entry.configure(font="TkFixedFont")
        self.username_entry.configure(selectbackground="blue")
        self.username_entry.configure(selectforeground="white")

        self.password_label = tk.Label(self.Labelframe1)
        self.password_label.place(relx=0.07, rely=0.406, height=40, width=192
                , bordermode='ignore')
        self.password_label.configure(activebackground="#f9f9f9")
        self.password_label.configure(background="#82d8c1")
        self.password_label.configure(font="-family {gothic} -size 14")
        self.password_label.configure(foreground="#fff")
        self.password_label.configure(relief="groove")
        self.password_label.configure(text='''Mot de passe''')
        

        self.password_entry = tk.Entry(self.Labelframe1)
        self.password_entry.place(relx=0.067, rely=0.519, height=37
                , relwidth=0.753, bordermode='ignore')
        self.password_entry.configure(background="white")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(selectbackground="blue")
        self.password_entry.configure(selectforeground="white")
        self.password_entry.configure(show='*')

        self.forget_pass_btn = tk.Button(self.Labelframe1)
        self.forget_pass_btn.place(relx=0.32, rely=0.678, height=25, width=150
                , bordermode='ignore')
        self.forget_pass_btn.configure(activebackground="#fff")
        self.forget_pass_btn.configure(activeforeground="#82d8c1")
        self.forget_pass_btn.configure(background="#fff")
        self.forget_pass_btn.configure(font="-family {courier 10 pitch} -size 13")
        self.forget_pass_btn.configure(foreground="#ff333a")
        self.forget_pass_btn.configure(relief="groove")
        self.forget_pass_btn.configure(text='''Passe oublié''')

        self.login_btn = tk.Button(self.Labelframe1)
        self.login_btn.place(relx=0.147, rely=0.83, height=35, width=160
                , bordermode='ignore')
        self.login_btn.configure(activebackground="#fff")
        self.login_btn.configure(activeforeground="#82d8c1")
        self.login_btn.configure(background="#82d8c1")
        self.login_btn.configure(font="-family {courier 10 pitch} -size 13")
        self.login_btn.configure(foreground="#fff")
        self.login_btn.configure(relief="groove")
        self.login_btn.configure(text='''Se connecter''')
        self.login_btn.configure(state='normal')
        self.login_btn.configure(command = self._get_login_value)

        self.Labelframe1_1 = tk.LabelFrame(top)
        self.Labelframe1_1.place(relx=0.017, rely=0.067, relheight=0.878
                , relwidth=0.45)
        self.Labelframe1_1.configure(relief='groove')
        self.Labelframe1_1.configure(font="-family {gothic} -size 14")
        self.Labelframe1_1.configure(text='''Creation de compte''')
        self.Labelframe1_1.configure(background="#82d8c1")

        self.nw_username_label = tk.Label(self.Labelframe1_1)
        self.nw_username_label.place(relx=0.07, rely=0.101, height=37, width=163
                , bordermode='ignore')
        self.nw_username_label.configure(activebackground="#f9f9f9")
        self.nw_username_label.configure(background="#82d8c1")
        self.nw_username_label.configure(font="-family {gothic} -size 14")
        self.nw_username_label.configure(foreground="#fff")
        self.nw_username_label.configure(relief="groove")
        self.nw_username_label.configure(text='''Utilisateur''')

        self.nw_username_entry = tk.Entry(self.Labelframe1_1)
        self.nw_username_entry.place(relx=0.067, rely=0.192, height=37
                , relwidth=0.837, bordermode='ignore')
        self.nw_username_entry.configure(background="white")
        self.nw_username_entry.configure(font="TkFixedFont")
        self.nw_username_entry.configure(selectbackground="blue")
        self.nw_username_entry.configure(selectforeground="white")

        self.nw_pass_label = tk.Label(self.Labelframe1_1)
        self.nw_pass_label.place(relx=0.07, rely=0.354, height=35, width=173
                , bordermode='ignore')
        self.nw_pass_label.configure(activebackground="#f9f9f9")
        self.nw_pass_label.configure(background="#82d8c1")
        self.nw_pass_label.configure(font="-family {gothic} -size 14")
        self.nw_pass_label.configure(foreground="#fff")
        self.nw_pass_label.configure(relief="groove")
        self.nw_pass_label.configure(text='''Mot de passe''')

        self.nw_password_entry = tk.Entry(self.Labelframe1_1)
        self.nw_password_entry.place(relx=0.067, rely=0.441, height=37
                , relwidth=0.837, bordermode='ignore')
        self.nw_password_entry.configure(background="white")
        self.nw_password_entry.configure(font="TkFixedFont")
        self.nw_password_entry.configure(selectbackground="blue")
        self.nw_password_entry.configure(selectforeground="white")

        self.sinup_btn = tk.Button(self.Labelframe1_1)
        self.sinup_btn.place(relx=0.144, rely=0.83, height=35, width=160
                , bordermode='ignore')
        self.sinup_btn.configure(activebackground="#fff")
        self.sinup_btn.configure(activeforeground="#82d8c1")
        self.sinup_btn.configure(background="#82d8c1")
        self.sinup_btn.configure(font="-family {courier 10 pitch} -size 13")
        self.sinup_btn.configure(foreground="#fff")
        self.sinup_btn.configure(relief="groove")
        self.sinup_btn.configure(text='''Nouveau Compte''')

        self.secret_label = tk.Label(self.Labelframe1_1)
        self.secret_label.place(relx=0.081, rely=0.565, height=35, width=173
                , bordermode='ignore')
        self.secret_label.configure(activebackground="#f9f9f9")
        self.secret_label.configure(background="#82d8c1")
        self.secret_label.configure(font="-family {gothic} -size 14")
        self.secret_label.configure(foreground="#fff")
        self.secret_label.configure(relief="groove")
        self.secret_label.configure(text='''Secret''')
        self.tooltip_font = "TkDefaultFont"
        self.secret_label_tooltip = \
        ToolTip(self.secret_label, self.tooltip_font, '''en cas de mot de passe oublié''')

        self.secret_entry = tk.Entry(self.Labelframe1_1)
        self.secret_entry.place(relx=0.081, rely=0.646, height=37, relwidth=0.837
                , bordermode='ignore')
        self.secret_entry.configure(background="white")
        self.secret_entry.configure(cursor="fleur")
        self.secret_entry.configure(font="TkFixedFont")
        self.secret_entry.configure(selectbackground="blue")
        self.secret_entry.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.583, rely=0.911, height=15, width=219)
        self.Label1.configure(text='''Secure Login by BorisBob''')
    


    def _get_login_value(self):

        if len(self.password_entry.get()) > 3 and len(self.username_entry.get()) > 3 :
            pass_value = self.password_entry.get()
            username_value = self.username_entry.get()
            #print(username_value,' : ',pass_value)
            
            LoginSignup._password = pass_value
            LoginSignup._username = username_value

            if LoginSignup._username == 'boris' and LoginSignup._password  == 'leponge':
                login_destry()
                main_laucnher()
            else:
                erro_title = 'Informations Incorrecte'
                error_msg='Veuillez enttrez un nom d\'Utilisateur et mot de passe correcte'
                show_warming(erro_title, error_msg)
        else:
            c = show_yes_no()
            print(c)

def login_gui_launcher():
    global app
    app = tkinter.Tk()
    pop_login = LoginSignup(app)
    app.mainloop()


def login_destry():
        app.destroy()

if __name__ == '__main__':    
    login_gui_launcher()