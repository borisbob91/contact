from interface.tkinker_import import *
from interface.support import *

from models.models import UserModel

import session_data



class ContactListGui:
    def __init__(self, top):
        self.contact_list_frame = tk.LabelFrame(top)
        self.contact_list_frame.place(relx=0.0, rely=0.151, relheight=0.822
                , relwidth=0.318)
        self.contact_list_frame.configure(relief='groove')
        self.contact_list_frame.configure(text='''Liste de Contacts''')

        self.Scrolledlistbox1 = ScrolledListBox(self.contact_list_frame)
        self.Scrolledlistbox1.place(relx=0.034, rely=0.075, relheight=0.857
                , relwidth=0.952, bordermode='ignore')
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="blue")
        self.Scrolledlistbox1.configure(selectforeground="white")
        self.Scrolledlistbox1.bind('<<ListboxSelect>>', self.selected)


        self.Scrolledlistbox1.insert( 1 , "Bread : 0759188395".center(34, '-') )

        

        self.list_fresh_btn = ttk.Button(self.contact_list_frame)
        self.list_fresh_btn.place(relx=0.293, rely=0.943, height=22, width=114
                , bordermode='ignore')
        self.list_fresh_btn.configure(takefocus="")
        self.list_fresh_btn.configure(text='''Actualiser''')

        self.TLabel1 = ttk.Label(self.contact_list_frame)
        self.TLabel1.place(relx=0.076, rely=0.04, height=13, width=114
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Nom & Prénoms''')

        self.TSeparator1 = ttk.Separator(self.contact_list_frame)
        self.TSeparator1.place(relx=0.49, rely=0.028, relheight=0.051
                , bordermode='ignore')
        self.TSeparator1.configure(orient="vertical")

        self.TLabel1_1 = ttk.Label(self.contact_list_frame)
        self.TLabel1_1.place(relx=0.545, rely=0.04, height=13, width=124
                , bordermode='ignore')
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="TkDefaultFont")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Numéro mobile''')
        self.show_contact()

    def show_contact(self):
        current_user = UserModel(session_data.session_username)
        
        if current_user.user_is_valide() :
            contact_list = current_user.get_contact_list()
            i = 2
            for contact in contact_list:
                self.Scrolledlistbox1.insert( i , f"{i} | {contact[1]} {contact[2]} | {contact[3]}")
                i += 1

    def selected(self):
        resultat = self.Scrolledlistbox1.selection_get()

        