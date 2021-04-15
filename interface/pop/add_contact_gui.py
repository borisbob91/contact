from interface.tkinker_import import *

from interface.support import *

from interface.message_box import show_info 
from argparse import FileType

class PopMenu:
    def __init__(self, top):
        _app_widht  = 912
        _app_height = 663

        sub_window_x = _app_widht // 2
        sub_window_y = _app_height // 2

        _screen_x = int(top.winfo_screenwidth())
        _screen_y = int(top.winfo_screenheight())

        _posi_x = (_app_widht // 2) - (sub_window_x // 2)
        _posi_y = (_app_height // 2) - (sub_window_y // 2)

        top.title('Ajout nouveau contact')
        top.geometry(f"{sub_window_x}x{sub_window_y}+{sub_window_x}+{sub_window_y}")
        top.resizable(False, False)

        self.name_label = tk.Label(top)
        self.name_label.place(relx=0.013, rely=0.11, height=23, width=115)
        self.name_label.configure(font="-family {gothic} -size 14")
        self.name_label.configure(text='''Nom :''')

        self.prenoms_label = tk.Label(top)
        self.prenoms_label.place(relx=0.065, rely=0.262, height=23, width=115)
        self.prenoms_label.configure(activebackground="#f9f9f9")
        self.prenoms_label.configure(font="-family {gothic} -size 14")
        self.prenoms_label.configure(text='''Prénoms :''')

        self.numero_label = tk.Label(top)
        self.numero_label.place(relx=0.059, rely=0.387, height=23, width=115)
        self.numero_label.configure(activebackground="#f9f9f9")
        self.numero_label.configure(cursor="fleur")
        self.numero_label.configure(font="-family {gothic} -size 14")
        self.numero_label.configure(text='''Numéro :''')

        self.name_entry = tk.Entry(top)
        self.name_entry.place(relx=0.326, rely=0.098, height=27, relwidth=0.535)
        self.name_entry.configure(background="white")
        self.name_entry.configure(font="-family {gothic} -size 12")

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.326, rely=0.229, height=27, relwidth=0.535)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(cursor="fleur")
        self.Entry1_1.configure(font="-family {gothic} -size 12")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(relx=0.328, rely=0.378, height=27, relwidth=0.535)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(font="-family {gothic} -size 12")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.Button1 = ttk.Button(top)
        self.Button1.place(relx=0.448, rely=0.866, height=25, width=140)
        self.Button1.configure(text='''Valider''')
        self.Button1.configure(command = self._add_contact)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.087, rely=0.61, height=25, width=90)
        self.Button2.configure(cursor="fleur")
        self.Button2.configure(font="-family {gothic} -size 12")
        self.Button2.configure(text='''Photo''', command=self._get_photo)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.093, rely=0.872, height=25, width=110)
        self.Button3.configure(text='''Annuler''')
        self.Button3.configure(command= top.destroy)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.413, rely=0.518, height=85, width=159)
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(relief="ridge")
        self.Label2.configure(text='''Label''')

    def _add_contact(self):
        c_name_value = self.name_entry.get()
        c_last_name = self.prenoms_entry.get()
        c_number = self.numero_entry.get()
        global c_photo
        c_photo = ''

        show_info('info', f'contact data {c_name_value, c_photo}')
        pop.mainloop()

    def _get_photo(self):
        c_photo = filedialog.askopenfile(parent= pop ,initialdir="/", title = 'select photo', \
            filetypes=(("photo png", "*.png"), ("photo jpg", "*.jpg"), ("photo gif", ".gif") ) )

    def  select_photo(self):
        self._get_photo()


def pop_menu_launcher():
        global pop 
        pop = tk.Toplevel()
        pop_menu = PopMenu(pop)
        pop.mainloop()

def pop_menu_destroy():
    pop.destroy()

if __name__ == '__main__':

    pop_menu()