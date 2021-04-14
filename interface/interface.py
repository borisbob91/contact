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



class Interface:

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

        window_x = Interface._app_widht
        window_y = Interface._app_height

        _posi_x = (_screen_x // 2) - (window_x // 2)
        _posi_y = (_screen_y // 2) - (window_y // 2)
        
        """__________________App Config zone______________________ """
    
        top.geometry(f"{Interface._app_widht}x{Interface._app_height}+{_posi_x }+{_posi_y}")
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
        self.sub_menu3.add_command(label="apropos", command=self.__show_about_menu)
        self.sub_menu3.add_command(label='contact')
        self.sub_menu3.add_command(label='Aide', command=self.__show_help_menu)

        

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
        

    """__________________Show help templates zone______________________ """
    def __show_about_menu(self):
        about = tkinter.Toplevel()

        sub_window_x = Interface._app_widht // 2
        sub_window_y = Interface._app_height // 2

        _screen_x = int(about.winfo_screenwidth())
        _screen_y = int(about.winfo_screenheight())

        _posi_x = (Interface._app_widht // 2) - (sub_window_x // 2)
        _posi_y = (Interface._app_height // 2) - (sub_window_y // 2)
        
        about.title('Apropos de l\'auteur')
        about.geometry(f"{sub_window_x}x{sub_window_y}+{sub_window_x}+{sub_window_y}")
        about.resizable(False, False)
        lb = tkinter.Label(about, text='bonjour je suis l\'auteur ')
        lb.pack()

    def __show_help_menu(self):
        helps = tkinter.Toplevel()

        sub_window_x = Interface._app_widht // 2
        sub_window_y = Interface._app_height // 2

        _screen_x = int(helps.winfo_screenwidth())
        _screen_y = int(helps.winfo_screenheight())

        _posi_x = (Interface._app_widht // 2) - (sub_window_x // 2)
        _posi_y = (Interface._app_height // 2) - (sub_window_y // 2)
        
        helps.title('demande d\'aide')
        helps.geometry(f"{sub_window_x}x{sub_window_y}+{sub_window_x}+{sub_window_y}")
        helps.resizable(False, False)
        lb = tkinter.Label(helps, text='bonjour, Vous avez besoin d\'aide ?')
        lb.pack()


def main_laucnher():
    global main_app
    main_app = tkinter.Tk()
    global main_window
    main_window = Interface(main_app)
    main_app.mainloop()

def main_destroy():
    main_app.destroy()


if __name__ == '__main__':
        import main
        