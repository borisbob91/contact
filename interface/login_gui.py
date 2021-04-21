#! usr/bin/env python3
# coding: utf-8

from .tkinker_import import *
from .support import *
from .tooltip import ToolTip
#from .interface import Interface
from interface.interface import main_laucnher
from interface.message_box import (show_warming, show_info, 
                                    show_error, show_ask_string)
from interface.about_gui import about_gui_launcher

from models import UserModel

import session_data
import color

session_username = 'BotUser'

class LoginSignup:
    _password = ''
    _username = ''
    _login_min = 3
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
        top.configure(background=color.bgColor)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#8fefd6',fg='#fff')
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu, label="aide")
        self.sub_menu.add_command(label="Auteur", command=about_gui_launcher)

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.483, rely=0.067, relheight=0.744
                , relwidth=0.5)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {gothic} -size 14")
        self.Labelframe1.configure(text='''Connexion''')
        self.Labelframe1.configure(background=color.bgColor)

        self.username_label = tk.Label(self.Labelframe1)
        self.username_label.place(relx=0.07, rely=0.101, height=40, width=182
                , bordermode='ignore')
        self.username_label.configure(activebackground="#f9f9f9")
        self.username_label.configure(background=color.bgColor)
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
        self.password_label.configure(background=color.bgColor)
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
        self.forget_pass_btn.configure(activeforeground=color.bgColor)
        self.forget_pass_btn.configure(background="#fff")
        self.forget_pass_btn.configure(font="-family {courier 10 pitch} -size 13")
        self.forget_pass_btn.configure(foreground="#ff333a")
        self.forget_pass_btn.configure(relief="groove")
        self.forget_pass_btn.configure(text='''Passe oublié''', command= self._reset_password)

        self.login_btn = tk.Button(self.Labelframe1)
        self.login_btn.place(relx=0.147, rely=0.83, height=35, width=160
                , bordermode='ignore')
        self.login_btn.configure(activebackground="#fff")
        self.login_btn.configure(activeforeground=color.bgColor)
        self.login_btn.configure(background=color.bgColor)
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
        self.Labelframe1_1.configure(background=color.bgColor)

        self.nw_username_label = tk.Label(self.Labelframe1_1)
        self.nw_username_label.place(relx=0.07, rely=0.101, height=37, width=163
                , bordermode='ignore')
        self.nw_username_label.configure(activebackground="#f9f9f9")
        self.nw_username_label.configure(background=color.bgColor)
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
        self.nw_pass_label.configure(background=color.bgColor)
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
        self.sinup_btn.configure(activeforeground=color.bgColor)
        self.sinup_btn.configure(background=color.bgColor)
        self.sinup_btn.configure(font="-family {courier 10 pitch} -size 13")
        self.sinup_btn.configure(foreground="#fff")
        self.sinup_btn.configure(relief="groove")
        self.sinup_btn.configure(text='''Nouveau Compte''', command=self._get_new_user)

        self.secret_label = tk.Label(self.Labelframe1_1)
        self.secret_label.place(relx=0.081, rely=0.565, height=35, width=173
                , bordermode='ignore')
        self.secret_label.configure(activebackground="#f9f9f9")
        self.secret_label.configure(background=color.bgColor)
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

        

        self.cancel_login_btn = tk.Button(top)
        self.cancel_login_btn.place(relx=0.617, rely=0.831, height=25, width=110)

        self.cancel_login_btn.configure(background="#d82b37")
        self.cancel_login_btn.configure(font="-family {clean} -size 12")
        self.cancel_login_btn.configure(foreground="#fff")
        self.cancel_login_btn.configure(highlightcolor="#ffffff")
        self.cancel_login_btn.configure(text='''Quitter''', command=login_destry)

        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.583, rely=0.911, height=15, width=219)
        self.Label1.configure(text='''Secure Login by BorisBob''')

    def _get_login_value(self):
        
        if len(self.password_entry.get()) > LoginSignup._login_min and \
        len(self.username_entry.get()) > LoginSignup._login_min :
            pass_value = self.password_entry.get()
            username_value = self.username_entry.get()
            #print(username_value,' : ',pass_value)

            user_input = UserModel(username_value.lower(), pass_value)
            data_user = user_input.user_validator()

            if data_user['user'] != None:
                global session_username
                session_username = data_user['user'][0]
                session_data.session_username = data_user['user'][0]
                login_destry()
                main_laucnher()
            else:
                erro_title = 'Login Error'
                error_msg='Les identifiants saisies sont incorrectes'
                show_error(erro_title, error_msg)
        else:
            erro_title = 'Attentions'
            error_msg='Veuillez enttrez un nom d\'Utilisateur et mot de passe'
            show_warming(erro_title, error_msg)

    def _get_new_user(self):

        if len(self.nw_username_entry.get()) > LoginSignup._login_min and \
        len(self.nw_password_entry.get()) > LoginSignup._login_min and \
        len(self.secret_entry.get()) >= 4 :

            username_value = self.nw_username_entry.get()
            pass_value = self.nw_password_entry.get()
            secret_value = self.secret_entry.get()
            

            new_user = UserModel(username_value.lower(), pass_value, secret_value)

            new_user.checking_data()
            
            req = new_user.add_user()
            
            if req :
                self.nw_username_entry.delete(0, len(username_value))
                self.nw_password_entry.delete(0, len(pass_value))
                self.secret_entry.delete(0, len(secret_value))
            

        else :
            erro_title = 'Attentions'
            error_msg='Veuillez remplir les champs ci-dessous'
            show_warming(erro_title, error_msg)

    def _reset_password(self):
        username_value = self.username_entry.get()

        user = UserModel(username_value.lower())
        
        if len(username_value) > 3 :
            if user.user_is_valide():
                response = show_ask_string('Reinitialisation de passe', 'veuillez entre le "secret" lors de la creation de votre compte')
                validate = user.reset_password_validate(response)
                if validate:
                    show_info('Login data', f'Vos Information de connexion \n Username: {validate[1]} \n PassWord: {validate[2]} \
                         \n Vous pouvez vous connecter !')
                else:
                    show_warming('Erreur de donnée', 'Le secret saisie n\'est pas le bon! \n Essayer à nouveau !')

            else:
                show_warming('Erreur de donnée', 'Veuillez entre un nom d\'utisateur correcte avant de reinitialiser le mot de passe !')
        else:
            show_warming('Alerte', 'Veuillez entre un nom d\'utisateur correcte avant de reinitialiser le mot de passe !')


def login_gui_launcher():
    global app
    app = tkinter.Tk()
    pop_login = LoginSignup(app)
    app.mainloop()


def login_destry():
        app.destroy()

if __name__ == '__main__':    
    login_gui_launcher()