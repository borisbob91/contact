#! /usr/bin/env python

from interface.tkinker_import import *

from interface.support import *

from interface.tooltip import ToolTip
from interface.contact_gui import ContactGui
from interface.import_export_gui import ImportExport
from interface.time_gui import TimeGui
from interface.session_gui import SessionGui
from interface.Search_gui import SearchGui
from interface.contact_list_gui import ContactListGui

from interface.pop.add_contact_gui import pop_menu



class MainApp:

    _app_widht  = 912
    _app_height = 663

    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'
        _app_bgcolor = "#88d8b8"
        _active_bg = "#5cfaff"
        _active_ft = "#ffffff"

        _screen_x = int(top.winfo_screenwidth())
        _screen_y = int(top.winfo_screenheight())

        window_x = MainApp._app_widht
        window_y = MainApp._app_height

        _posi_x = (_screen_x // 2) - (window_x // 2)
        _posi_y = (_screen_y // 2) - (window_y // 2)
        
        """__________________App Config zone______________________ """
    
        top.geometry(f"{MainApp._app_widht}x{MainApp._app_height}+{_posi_x }+{_posi_y}")
        top.minsize(1, 1)
        top.maxsize(1585, 870)
        top.resizable(1,  1)
        top.title("Gestionnaire de Contact")
        top.configure(background=_app_bgcolor)

        """__________________Menu Bar templates zone______________________ """

        menu_list = [
            ('Fichier', "Importer", "Exporter","Quitter" ),
            ('Edition', "Ajouter", "Supprimer","Modifier"),
            ("Aide", "apropos", 'contact')
        ]

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        self.sub_menu = tk.Menu(top, tearoff=0)
            
        self.menubar.add_cascade(menu=self.sub_menu, activebackground=_active_bg,  activeforeground=_active_ft,
                label='Fichier')
        self.sub_menu.add_command(label="Importer")
        self.sub_menu.add_command(label="Exporter")
        self.sub_menu.add_command(label="Quitter", command= top.quit)

        self.sub_menu2 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu2, activebackground=_active_bg,  activeforeground=_active_ft,
                label='Edition')
        self.sub_menu2.add_command(label="Ajouter", command=pop_menu)
        self.sub_menu2.add_command(label="Supprimer")
        self.sub_menu2.add_command(label="Modifier")

        self.sub_menu3 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu3, activebackground=_active_bg,  activeforeground=_active_ft,
                label="Aide")
        self.sub_menu3.add_command(label="apropos")
        self.sub_menu3.add_command(label='contact')
        self.sub_menu3.add_command(label='Aide', command=self.show_about_menu)

        

        """__________________Search templates zone______________________ """
        self.search_gui = SearchGui(top)

        
        """__________________List contacts templates zone______________________ """

        self.contact_list_gui = ContactListGui(top)

        """__________________List contacts templates zone______________________ """
  
        self.contact_gui = ContactGui(top)

        """__________________List import export templates zone______________________ """

        self.import_export_gui = ImportExport(top)

        """__________________List times / dates templates zone______________________ """

        self.time_gui = TimeGui(top)

        """__________________List session templates zone______________________ """

        self.session_info_gui = SessionGui(top)
    """__________________SubMenu templates zone______________________ """
    
    def show_about_menu(self):
        about = tkinter.Toplevel()

        sub_window_x = MainApp._app_widht // 2
        sub_window_y = MainApp._app_height // 2

        _screen_x = int(about.winfo_screenwidth())
        _screen_y = int(about.winfo_screenheight())

        _posi_x = (MainApp._app_widht // 2) - (sub_window_x // 2)
        _posi_y = (MainApp._app_height // 2) - (sub_window_y // 2)
        
        about.title('demande d\'aide')
        about.geometry(f"{sub_window_x}x{sub_window_y}+{sub_window_x}+{sub_window_y}")
        about.resizable(False, False)
        lb = tkinter.Label(about, text='bonjour')
        lb.pack()

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.0, rely=0.151, relheight=0.822
                , relwidth=0.318)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(text='''Liste de Contacts''')

        self.Scrolledlistbox1 = ScrolledListBox(self.Labelframe1)
        self.Scrolledlistbox1.place(relx=0.034, rely=0.075, relheight=0.857
                , relwidth=0.952, bordermode='ignore')
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="blue")
        self.Scrolledlistbox1.configure(selectforeground="white")

        self.TButton1_1 = ttk.Button(self.Labelframe1)
        self.TButton1_1.place(relx=0.293, rely=0.943, height=22, width=114
                , bordermode='ignore')
        self.TButton1_1.configure(takefocus="")
        self.TButton1_1.configure(text='''Actualiser''')

        self.TLabel1 = ttk.Label(self.Labelframe1)
        self.TLabel1.place(relx=0.076, rely=0.04, height=13, width=114
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Nom & Prénoms''')

        self.TSeparator1 = ttk.Separator(self.Labelframe1)
        self.TSeparator1.place(relx=0.49, rely=0.028, relheight=0.051
                , bordermode='ignore')
        self.TSeparator1.configure(orient="vertical")

        self.TLabel1_1 = ttk.Label(self.Labelframe1)
        self.TLabel1_1.place(relx=0.545, rely=0.04, height=13, width=124
                , bordermode='ignore')
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="TkDefaultFont")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Numéro mobile''')

    """__________________SubMenu templates zone______________________ """





if __name__ == '__main__':
        import main
        