from interface.tkinker_import import *
from interface.support import *

from models.models import UserModel, ContactModel
from myutils import Contact_Struct, clean_string
from session_data import read_token
from config import BASE_DIR, IMAGES_DIR
from interface.pop.add_contact_gui import pop_menu_launcher
from .tooltip import ToolTip
from myutils import  ImageEdit
from .message_box import *
from PIL import Image, ImageTk
from os import path
from copy import deepcopy
import config
import time
import color
from typing import Union, NoReturn


class ContactInfoGui:
    def __init__(self, top):
        global file_img
        file_img = None
        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.329, rely=0.151, relheight=0.43
                , relwidth=0.658)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(text='''Detail contact''')

        self.Label_nom = tk.Label(self.Labelframe2)
        self.Label_nom.place(relx=0.05, rely=0.112, height=15, width=89
                        , bordermode='ignore')
        self.Label_nom.configure(font="-family {gothic} -size 12")
        self.Label_nom.configure(text='''Nom :''')

        self.Label_prenoms = tk.Label(self.Labelframe2)
        self.Label_prenoms.place(relx=0.073, rely=0.305, height=15, width=89
                        , bordermode='ignore')
        self.Label_prenoms.configure(activebackground="#f9f9f9")
        self.Label_prenoms.configure(font="-family {gothic} -size 12")
        self.Label_prenoms.configure(text='''Prénoms :''')

        self.Label_numero = tk.Label(self.Labelframe2)
        self.Label_numero.place(relx=0.072, rely=0.495, height=15, width=89
                        , bordermode='ignore')
        self.Label_numero.configure(activebackground="#f9f9f9")
        self.Label_numero.configure(font="-family {gothic} -size 12")
        self.Label_numero.configure(text='''Numéro :''')

        self.Entry_nom = tk.Entry(self.Labelframe2)
        self.Entry_nom.place(relx=0.22, rely=0.07, height=37, relwidth=0.393
                        , bordermode='ignore')
        self.Entry_nom.configure(background="white")
        self.Entry_nom.configure(font="-family {gothic} -size 12")

        self.Entry_prenoms = tk.Entry(self.Labelframe2)
        self.Entry_prenoms.place(relx=0.218, rely=0.26, height=37, relwidth=0.393
                        , bordermode='ignore')
        self.Entry_prenoms.configure(background="white")
        self.Entry_prenoms.configure(cursor="fleur")
        self.Entry_prenoms.configure(font="-family {gothic} -size 12")
        self.Entry_prenoms.configure(selectbackground="blue")
        self.Entry_prenoms.configure(selectforeground="white")

        self.Entry_numero = tk.Entry(self.Labelframe2)
        self.Entry_numero.place(relx=0.215, rely=0.46, height=37, relwidth=0.393
                        , bordermode='ignore')
        self.Entry_numero.configure(background="white")
        self.Entry_numero.configure(font="-family {gothic} -size 12")
        self.Entry_numero.configure(selectbackground="blue")
        self.Entry_numero.configure(selectforeground="white")

        self.photo_contact = tk.Label(self.Labelframe2)

        self.contact_img_view()

        self.photo_contact.configure(relief="groove")
        self.photo_contact.configure(text='''Label''')
        self.photo_contact.place(relx=0.668, rely=0.081, height=155, width=139
                        , bordermode='ignore')

        self.TButton2 = ttk.Button(self.Labelframe2)
        self.TButton2.place(relx=0.68, rely=0.681, height=22, width=124
                        , bordermode='ignore')
        self.TButton2.configure(text='''Nouvelle photo''', command=self.change_photo)
        self.tooltip_font = "TkDefaultFont"
        self.TButton2_tooltip = \
                ToolTip(self.TButton2, self.tooltip_font, '''Ajouter photo de profil''')

        self.save_edit_btn = ttk.Button(self.Labelframe2)
        self.save_edit_btn.place(relx=0.368, rely=0.698, height=22, width=124
                        , bordermode='ignore')
        self.save_edit_btn.configure(takefocus="")
        self.save_edit_btn.configure(text='''Enrégistrer''', command = self.__save_edit)
        self.tooltip_font = "TkDefaultFont"
        self.save_edit_btn_tooltip = \
            ToolTip(self.save_edit_btn, self.tooltip_font, '''Enrégistrer les modifications effectuées ''')

        self.delete_contact_btn = ttk.Button(self.Labelframe2)
        self.delete_contact_btn.place(relx=0.083, rely=0.698, height=22, width=124
                        , bordermode='ignore')
        self.delete_contact_btn.configure(takefocus="")
        self.delete_contact_btn.configure(text='''Supprimier''', command = self.delete_contact)
        self.tooltip_font = "TkDefaultFont"
        self.delete_contact_btn_tooltip = \
                ToolTip(self.delete_contact_btn, self.tooltip_font, '''Supprimer le contact de la liste''')

        self.add_contact_btn = ttk.Button(self.Labelframe2)
        self.add_contact_btn.place(relx=0.367, rely=0.842, height=22, width=124
                        , bordermode='ignore')
        self.add_contact_btn.configure(takefocus="")
        self.add_contact_btn.configure(text='''Ajouter nouveau''', command=pop_menu_launcher)
        self.tooltip_font = "TkDefaultFont"
        self.add_contact_btn_tooltip = \
                ToolTip(self.add_contact_btn, self.tooltip_font, '''ajouter un nouveau contact''')

        global photo_file
        photo_file = False
        self.photo_file = None
        self.file_img = None


    def contact_img_view(self, img_source = f'{IMAGES_DIR}/img.jpg' ) -> NoReturn:
        load = Image.open(img_source)
        load.thumbnail((139, 155))
        global _img0
        _img0 = ImageTk.PhotoImage(load)
        self.photo_contact.configure(image=_img0)


    def _get_selected(self):
        tmp_selection = contact_getted
        return tmp_selection


    def __validate_change(self):
        '''Indique si une modification a eu lieu sur \n
        le [nom, prenoms,numero,photo]  '''

        e_name = self.Entry_nom.get().lower()
        e_last_name = self.Entry_prenoms.get().lower()
        e_number = self.Entry_numero.get()
        e_photo = self.photo_file


        if self.contact_getted:

            if (self.contact_getted.c_nom.lower() != e_name or \
                self.contact_getted.c_prenoms.lower() != e_last_name \
                or self.contact_getted.c_numero != e_number ) or e_photo :
                #NewContact = ContactModel(e_name, e_last_name, e_number, e_photo )
                if self.photo_file:
                #e_photo = contact_getted.c_photo
                    print('photo changé')
                    print("entry :", e_name,' ',e_last_name, ' ',e_number,' ', e_photo)

                    return 1, Contact_Struct(*[self.contact_getted.c_id, e_name, e_last_name, e_number, e_photo, self.contact_getted.c_user_id])
                else:
                    print('photo non changé')
                    print("entry :", e_name,' ',e_last_name, ' ',e_number,' ', e_photo)
                    return 0, Contact_Struct(*[self.contact_getted.c_id, e_name, e_last_name, e_number, self.contact_getted.c_photo, self.contact_getted.c_user_id])
            else:
                #print('aucune modification apportée')
                show_info('info', 'Auncune modification détectée !')
                raise  BaseException('aucune modification apportée')
        else:
            #print('impossible de modifier le contact , veuillez selectionnez un contact dans la liste')
            show_warming('Attention', 'Veuillez selectionnez un contact dans la liste! !')
            raise  BaseException('Veuillez selectionnez un contact dans la liste! ')

    def refresh_entry(self):
        self.Entry_nom.delete(0, tk.END)
        self.Entry_prenoms.delete(0, tk.END)
        self.Entry_numero.delete(0, tk.END)
        self.photo_file = None
        self.contact_getted = None
        self.contact_img_view()

    def __get_photo(self):
        """Selection de fichier photo """
        
        path_photo = filedialog.askopenfilename(initialdir=path.expanduser('~') +'/Images', title = 'select photo', \
            filetypes=(("photo png", "*.png"), ("photo jpg", "*.jpg"), ("photo gif", "*.gif"),("photo jpeg", "*.jpeg")))
        return path_photo

    def __show_photo(self):
        
        global img
        
        file_img = self.__get_photo()
        try:
            loaded = Image.open(file_img)
            global loaded_tmp
            loaded_tmp = loaded
        except :
            print('soucis d\'ouverture de l\'image ')
        else:
            loaded.thumbnail((140,150))
            img = ImageTk.PhotoImage(loaded)
            self.photo_contact.configure(image = img)

        return file_img

    def change_photo(self):
        self.photo_file = self.__show_photo()
        


    def __save_photo(self, file_name):

        image = loaded_tmp.convert('RGB')
        image = image.resize((150,  200))

        image.save((f'{config.IMAGES_DIR}/{file_name}.png'))

        return {}

    def __save_edit(self):
        """For save Edit in contact row"""
        
        status , contact_to_edit = self.__validate_change()
        print("status :", status, ' to edit', contact_to_edit)
        nom        = contact_to_edit.c_nom
        prenoms    = contact_to_edit.c_prenoms
        numero     = contact_to_edit.c_numero
        user_id    = contact_to_edit.c_user_id
        contact_id = contact_to_edit.c_id

        #CurrentUser = UserModel(session_data.session_username)
        CurrentUser = UserModel(read_token().u_name)
        updateContact = ContactModel(nom=nom, prenoms=prenoms, numero=numero , user_id=user_id ,\
         contact_id=contact_id )

        assert list(CurrentUser.get_id)[0] > 0 , ''' Attentions vous êtes pas connecté '''
        updateContact.set_id(CurrentUser.get_id[0])
        
        if status == 1:
            #print('il y a modification avec photo')
            extention ='png'
            image_path = contact_to_edit.c_photo
            destination = f'{config.IMAGES_DIR}/img_{contact_to_edit.c_id}.{extention}'

            new_photo = ImageEdit(image_path, (150,  200) , destination)
            succes = new_photo.save()
            if succes:
                updateContact.update_img()
                #print('photo edité')
            else:
                #print('photo non edité')
                pass

            if updateContact.update_valide() :
                update = updateContact.update()
                if update :
                    show_info('info', 'Information enregistré !')
                else:
                    show_error('error', 'problème lors de l\' enregistrement !')
            else:
                show_warming("error",'Le nom et Prénoms existes déja !')
        elif status == 0:
            #print('modification sans photo')

            if updateContact.update_valide() :
                update = updateContact.update()
                if update :
                    show_info('info', 'Information enregistré !')
                    self._show_contact()
                else:
                    show_error('error', 'Le nom et Prénoms existes déja !')
                #updateContact.update()
            else:
                show_warming("error",'Le nom et Prénoms existes déja !')
        else:
            show_info('attentions','veuillez selectionner un contact à modifier !')

        return self.refresh_entry()

    def delete_contact(self):
        """Delete a selected contact from ScrolListBox
        
        Keyword arguments: contact id, user id
        argument -- self.contact_id in the db, 
                    self.user_id for current User of the session
        Return: No return
        """
        
        if contact_getted:
            contact_id = contact_getted.c_id
            contact_user_id = contact_getted.c_user_id
            Contact_selected = ContactModel(contact_id = contact_id , user_id = contact_user_id)
            response = show_yes_no('attentions', 'Voulez vous supprimer ce contact ?')
            if response:
                request = Contact_selected.delete()
                if request:
                    show_info("info", 'contact supprimer avec succès !')
                    self.refresh_list()
                    self.refresh_entry()
                else:
                    show_warming("Attention", 'echec de suppression !')
        else:
            show_error('Erreur','veuillez selectionner un contact dans la liste')


class ContactListGui(ContactInfoGui):

    def __init__(self, top):
        super().__init__(top)
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
        self.Scrolledlistbox1.configure(selectbackground=color.bgColor)
        self.Scrolledlistbox1.configure(selectforeground=color.fontColor)
        self.Scrolledlistbox1.bind('<<ListboxSelect>>', self.selected)
        self.Scrolledlistbox1.insert( 0 , "Boris Bob : 0759188395".center(34, '-') )

        self.list_fresh_btn = ttk.Button(self.contact_list_frame)
        self.list_fresh_btn.place(relx=0.293, rely=0.943, height=22, width=114
                , bordermode='ignore')
        self.list_fresh_btn.configure(takefocus="")
        self.list_fresh_btn.configure(text='''Actualiser''', command= self.refresh_list)

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

        self.contact_getted = None
        self.dictionnaire = {}
        self._show_contact()
        global contact_getted
        contact_getted = None


    def _show_contact(self):
        current_user = UserModel(read_token().u_name)
        if current_user.user_is_valide():
            global contact_list
            contact_list = current_user.get_contact_list()
                
            index = 1
            for contact in contact_list:
                self.Scrolledlistbox1.insert( index , f"{index}.{contact[1].title()}")
                index +=1

            global contact_dic
            self.dictionnaire = contact_dic = self.make_dict_key(contact_list)
            # with open('contact.txt', 'a') as files:
                    # files.write(f"{self.dictionnaire }\n")
        
    def make_dict_key(self, contact_list : Union[list or tuple]):
            index = 1
            contact_name = []
            for contact in contact_list:
                contact = [i for i in contact]
                contact_clean = clean_string(contact)
                contact = deepcopy(contact_clean)
                c_struct = Contact_Struct(*contact[:6])

                name_key =  f'{index}_{c_struct.c_nom.lower()}'
                contact_name.append(name_key)
                index += 1
           
            contact_dic = {str(name):value for name, value in zip(contact_name, contact_list)}
            ContactListGui.contact_dict = contact_dic

            return contact_dic

    def selected(self, *args):

        selection = self.Scrolledlistbox1.selection_get().lower()
        contact_name = clean_string('_'.join(selection.split('.')))[0]
        assert len(selection)> 0, ''' mauvais selection '''
        #contact_name = selection.split('.')[0]
        #print("dict :",  contact_dic)
        if str(contact_name) in self.dictionnaire:
            finded = self.dictionnaire.get(str(contact_name))
            global contact_getted
            self.contact_getted = contact_getted = Contact_Struct(*finded)
        else:
            pass
        self._get_selected()
        self.Entry_nom.delete(0, tk.END)
        self.Entry_nom.insert(0, contact_getted.c_nom.title())

        self.Entry_prenoms.delete(0, tk.END)
        self.Entry_prenoms.insert(0, self.contact_getted.c_prenoms.title())

        self.Entry_numero.delete(0, tk.END)
        self.Entry_numero.insert(0, self.contact_getted.c_numero)

        try:

            load = Image.open(f'{IMAGES_DIR}/{self.contact_getted.c_photo}.jpg')
        except FileNotFoundError as e:
            try:
                load = Image.open(f'{IMAGES_DIR}/{contact_getted.c_photo}.png')
            except  FileNotFoundError as e:
                load = Image.open(f'{IMAGES_DIR}/img.jpg')
        finally:
            load.thumbnail((140,155))
            global _img0
            _img0 = ImageTk.PhotoImage(load)
            self.photo_contact.configure(image=_img0)

        return args

    def refresh_list(self):
        self.clear_list()
        self.refresh_entry()
        self._show_contact()

    def clear_list(self):
        self.Scrolledlistbox1.delete(1, tk.END)
    