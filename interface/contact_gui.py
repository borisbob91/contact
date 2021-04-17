from interface.tkinker_import import *
from interface.pop.add_contact_gui import pop_menu_launcher

from .tooltip import ToolTip
from PIL import Image, ImageTk

import os
import sys
from config import BASE_DIR, IMAGES_DIR


prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]

img = ''
class ContactGui:
       

        def __init__(self, top):
                self.Labelframe2 = tk.LabelFrame(top)
                self.Labelframe2.place(relx=0.329, rely=0.151, relheight=0.43
                , relwidth=0.658)
                self.Labelframe2.configure(relief='groove')
                self.Labelframe2.configure(text='''Detail contact''')

                self.Label1 = tk.Label(self.Labelframe2)
                self.Label1.place(relx=0.05, rely=0.112, height=15, width=89
                        , bordermode='ignore')
                self.Label1.configure(font="-family {gothic} -size 12")
                self.Label1.configure(text='''Nom :''')

                self.Label1_1 = tk.Label(self.Labelframe2)
                self.Label1_1.place(relx=0.073, rely=0.305, height=15, width=89
                        , bordermode='ignore')
                self.Label1_1.configure(activebackground="#f9f9f9")
                self.Label1_1.configure(font="-family {gothic} -size 12")
                self.Label1_1.configure(text='''Prénoms :''')

                self.Label1_2 = tk.Label(self.Labelframe2)
                self.Label1_2.place(relx=0.072, rely=0.495, height=15, width=89
                        , bordermode='ignore')
                self.Label1_2.configure(activebackground="#f9f9f9")
                self.Label1_2.configure(font="-family {gothic} -size 12")
                self.Label1_2.configure(text='''Numéro :''')

                self.Entry2 = tk.Entry(self.Labelframe2)
                self.Entry2.place(relx=0.22, rely=0.07, height=37, relwidth=0.393
                        , bordermode='ignore')
                self.Entry2.configure(background="white")
                self.Entry2.configure(font="-family {gothic} -size 12")

                self.Entry2_1 = tk.Entry(self.Labelframe2)
                self.Entry2_1.place(relx=0.218, rely=0.26, height=37, relwidth=0.393
                        , bordermode='ignore')
                self.Entry2_1.configure(background="white")
                self.Entry2_1.configure(cursor="fleur")
                self.Entry2_1.configure(font="-family {gothic} -size 12")
                self.Entry2_1.configure(selectbackground="blue")
                self.Entry2_1.configure(selectforeground="white")

                self.Entry2_2 = tk.Entry(self.Labelframe2)
                self.Entry2_2.place(relx=0.215, rely=0.46, height=37, relwidth=0.393
                        , bordermode='ignore')
                self.Entry2_2.configure(background="white")
                self.Entry2_2.configure(font="-family {gothic} -size 12")
                self.Entry2_2.configure(selectbackground="blue")
                self.Entry2_2.configure(selectforeground="white")


                '''self.photo_label = tk.Label(self.Labelframe2)
                self.photo_label.place(relx=0.658, rely=0.067, relheight=0.565
                , relwidth=0.252, bordermode='ignore', x = 0, y=0)
                self.photo_label.configure(borderwidth="2")
                self.photo_label.configure(relief="ridge")
                self.photo_label.configure(image = photo)'''

                self.photo_contact = tk.Label(self.Labelframe2)
                load = Image.open(f'{IMAGES_DIR}/img.jpg')
                load.thumbnail((139,155))

                global _img0
                _img0 = ImageTk.PhotoImage(load)
                self.photo_contact.configure(image=_img0)
                self.photo_contact.configure(relief="groove")
                self.photo_contact.configure(text='''Label''')
                self.photo_contact.place(relx=0.668, rely=0.081, height=155, width=139
                        , bordermode='ignore')

                self.TButton2 = ttk.Button(self.Labelframe2)
                self.TButton2.place(relx=0.68, rely=0.681, height=22, width=124
                        , bordermode='ignore')
                self.TButton2.configure(text='''Nouvelle photo''')
                self.tooltip_font = "TkDefaultFont"
                self.TButton2_tooltip = \
                ToolTip(self.TButton2, self.tooltip_font, '''Ajouter photo de profil''')

                self.save_edit_btn = ttk.Button(self.Labelframe2)
                self.save_edit_btn.place(relx=0.368, rely=0.698, height=22, width=124
                        , bordermode='ignore')
                self.save_edit_btn.configure(takefocus="")
                self.save_edit_btn.configure(text='''Enrégistrer''')
                self.tooltip_font = "TkDefaultFont"
                self.save_edit_btn_tooltip = \
                ToolTip(self.save_edit_btn, self.tooltip_font, '''Enrégistrer les modifications effectuées ''')

                self.delete_contact_btn = ttk.Button(self.Labelframe2)
                self.delete_contact_btn.place(relx=0.083, rely=0.698, height=22, width=124
                        , bordermode='ignore')
                self.delete_contact_btn.configure(takefocus="")
                self.delete_contact_btn.configure(text='''Supprimier''')
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