from interface.tkinker_import import *

from .tooltip import ToolTip
from tkinter import *
from .message_box import show_info, show_warming, show_error
from .contact_list_gui import ContactListGui
import session_data
from models import UserModel


class SearchGui(ContactListGui):
    
    def __init__(self, top):
        super().__init__(top)

        global is_by_name
        is_by_name = IntVar()
        global by_number
        by_number = IntVar()
        self.search_frame = tk.Frame(top)
        self.search_frame.place(relx=0.0, rely=0.015, relheight=0.128, relwidth=0.32)
        self.search_frame.configure(relief='groove')
        self.search_frame.configure(borderwidth="2")
        self.search_frame.configure(relief="groove")

        self.search_Entry = tk.Entry(self.search_frame)
        self.search_Entry.place(relx=0.034, rely=0.118, height=27, relwidth=0.911)
        self.search_Entry.configure(background="white")
        self.search_Entry.configure(cursor="xterm")
        self.search_Entry.configure(font="TkFixedFont")

        self.search_btn = ttk.Button(self.search_frame)
        self.search_btn.place(relx=0.239, rely=0.682, height=22, width=114)
        self.search_btn.configure(takefocus="")
        self.search_btn.configure(text='''Rechercher''')        
        self.search_btn.configure(command=self.get_search_value)   

        self.search_radio_btn = tk.Radiobutton(self.search_frame)
        self.search_radio_btn.place(relx=0.58, rely=0.471, relheight=0.2131, relwidth=0.37)
        self.search_radio_btn.configure(justify='left')
        self.search_radio_btn.configure(text='''Par nom''')
        self.search_radio_btn.configure(value = 1, variable=is_by_name, command= self.get_radio_value)

        self.search_radio_btn_1 = tk.Radiobutton(self.search_frame)
        self.search_radio_btn_1.place(relx=0.068, rely=0.471, relheight=0.2131, relwidth=0.37)
        self.search_radio_btn_1.configure(justify='left')
        self.search_radio_btn_1.configure(text='''Par Numero''')
        self.search_radio_btn_1.configure(value = 0, variable=is_by_name, command= self.get_radio_value)

        #messagbow : showerror, showinfo, showwarning, askyesno, askokcancel ...etc
    def show_message_box(self):
        messagebox.showwarning('Attentions:', "Veuillez entrez une valeur")

    def get_search_value(self):
        global current_user
        current_user = UserModel(session_data.session_username)
        value_enter = self.search_Entry.get()

        is_name = self.get_radio_value()
        if is_name :
            if not value_enter.isalpha():
                show_warming(title="Erreur", msg='cochez la bonne case de numero')
                assert value_enter.isalpha(), 'nom: <class alpha>'

            resultat = self.search_by_name(value_enter)
            self.clear_list()
            if not len(resultat) > 0 :
                self.Scrolledlistbox1.insert( 1 , f"Auncun resultat pour {value_enter}!")
            else:
                self._show_resultat(resultat)
        else:
            if not value_enter.isnumeric():
                show_warming(title="Erreur", msg='cochez la bonne case de nom')
                assert value_enter.isnumeric(), 'numero : <class numeric>'

            resultat = self.search_by_number(value_enter)
            self.clear_list()
            if not len(resultat) > 0 :
                self.Scrolledlistbox1.insert( 1 , f"Auncun resultat pour {value_enter} !")
            else:       
                self._show_resultat(resultat)

        return {}
       

    def get_radio_value(self):
        global is_name
        is_name = is_by_name.get()
        
        return is_name

    def search_by_name(self, word):
        return current_user.search_contact_by_name(word)
        
    def search_by_number(self, number):
        return current_user.search_contact_by_number(number)

    def _show_resultat(self, query_resultat=None):
        contact_name = list()

        global resultat_list
        resultat_list = query_resultat
        print(resultat_list)
        i = 1
        for contact in resultat_list:
            self.Scrolledlistbox1.insert( i , f"{i}.{contact[1]} {contact[2]}")
            i += 1
            contact_name.append(contact[1])

        global contact_dic
        contact_dic = {name:value for name, value in zip(contact_name,resultat_list)}
        return {}


