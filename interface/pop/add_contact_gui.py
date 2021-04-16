#coding: utf-8

from PIL import Image, ImageTk

from interface.tkinker_import import *
from interface.support import *

from models.models import ContactModel
from interface.message_box import show_info

from interface import login_gui
import config

class PopMenu:
    load_photo = None
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

        self.prenoms_entry = tk.Entry(top)
        self.prenoms_entry.place(relx=0.326, rely=0.229, height=27, relwidth=0.535)
        self.prenoms_entry.configure(background="white")
        self.prenoms_entry.configure(font="-family {gothic} -size 12")
        self.prenoms_entry.configure(selectbackground="blue")
        self.prenoms_entry.configure(selectforeground="white")

        self.numero_entry = tk.Entry(top)
        self.numero_entry.place(relx=0.328, rely=0.378, height=27, relwidth=0.535)
        self.numero_entry.configure(background="white")
        self.numero_entry.configure(font="-family {gothic} -size 12")
        self.numero_entry.configure(selectbackground="blue")
        self.numero_entry.configure(selectforeground="white")

        self.Button1 = ttk.Button(top)
        self.Button1.place(relx=0.448, rely=0.866, height=25, width=140)
        self.Button1.configure(text='''Valider''')
        self.Button1.configure(command = self._add_contact)

        self.select_photo_btn = tk.Button(top)
        self.select_photo_btn.place(relx=0.087, rely=0.61, height=25, width=90)
        self.select_photo_btn.configure(cursor="fleur")
        self.select_photo_btn.configure(font="-family {gothic} -size 12")
        self.select_photo_btn.configure(text='''Photo''', command=self._select_photo)

        self.cancel_btn = tk.Button(top)
        self.cancel_btn.place(relx=0.093, rely=0.872, height=25, width=110)
        self.cancel_btn.configure(text='''Annuler''')
        self.cancel_btn.configure(command= top.destroy)

        self.photo_view = tk.Label(top)
        self.photo_view.place(relx=0.413, rely=0.518, height=85, width=159)
        self.photo_view.configure(cursor="fleur")
        self.photo_view.configure(relief="ridge")
        self.photo_view.configure(text='''Label''')

    def _add_contact(self):
        c_name_value         = self.name_entry.get()
        c_last_name_value    = self.prenoms_entry.get()
        c_number_value       = self.numero_entry.get()
        c_photo              = PopMenu.load_photo
        user_id = 1

        if len(c_name_value) >= 2 and len(c_number_value) >= 3 :

            NewContact = ContactModel(nom =c_name_value, prenoms = c_last_name_value, \
                numero=c_number_value, photo= c_photo, user_id=user_id)

            if c_photo != None:

                last_id = NewContact.get_last_id
                NewContact.set_photo(f'img_{last_id + 1}')

            validate = NewContact.contact_validator()

            if validate.get('name') or validate.get('number'):

                if validate.get('name'):
                    show_info('error', 'Le nom entré exite déja :')
                else :
                    show_info('error', 'Le numero entré exite déja :')

            else:
                print('on continue l\'enregistrement ici')
                print(f'nom :{NewContact.get_name} number: {NewContact.get_number} photo: {NewContact.get_photo}\
                    sessionId: {login_gui.session_username} sId: {user_id}')

                sessionId = login_gui.session_username
                if sessionId != 'BotUser':
                    #get user id
                    NewContact.save()
                    print('saved !')
                else:
                    print('not ready to save')



        else:
            show_info('error', 'veuillez fournit au moin un nom et numero ')
            pop.mainloop()


        pop.mainloop()

    def __get_photo(self):
        path_photo = filedialog.askopenfilename(parent = pop ,initialdir="/", title = 'select photo', \
            filetypes=(("photo png", "*.png"), ("photo jpg", "*.jpg"), ("photo gif", ".gif"),("photo jpeg", "*.jpeg") ) )
        PopMenu.load_photo = path_photo

    def _select_photo(self):
        self.__get_photo()

        if PopMenu.load_photo != None:
            self.__show_photo()
            
    def __save_user_photo(self, photo_path, file_name = '1'):
        imag_file = Image.open(photo_path)
        imag_file = imag_file.convert('RGB')
        imag_file.save((f'{config.IMAGES_DIR}/img_{file_name}.png'))

    def __show_photo(self):
        global img
        loaded = Image.open(PopMenu.load_photo)
        loaded.thumbnail((130,140))
        img = ImageTk.PhotoImage(loaded)
        self.photo_view.configure(image = img)

    def contact_valide(self):
        name   = self.name_entry.get()
        number = self.numero_entry.get()


def pop_menu_launcher():
        global pop 
        pop = tk.Toplevel()
        pop_menu = PopMenu(pop)
        pop.mainloop()

def pop_menu_destroy():
    pop.destroy()

if __name__ == '__main__':

    pop_menu()