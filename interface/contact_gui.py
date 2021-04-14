from interface.tkinker_import import *

import  os 
from .tooltip import ToolTip


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

                self.Canvas1 = tk.Canvas(self.Labelframe2)
                self.Canvas1.place(relx=0.658, rely=0.067, relheight=0.565
                , relwidth=0.252, bordermode='ignore')
                self.Canvas1.configure(borderwidth="2")
                self.Canvas1.configure(relief="ridge")
                self.Canvas1.configure(selectbackground="blue")
                self.Canvas1.configure(selectforeground="white")
                

                self.TButton2 = ttk.Button(self.Labelframe2)
                self.TButton2.place(relx=0.68, rely=0.681, height=22, width=124
                        , bordermode='ignore')
                self.TButton2.configure(text='''Nouvelle photo''')
                self.tooltip_font = "TkDefaultFont"
                self.TButton2_tooltip = \
                ToolTip(self.TButton2, self.tooltip_font, '''Ajouter photo de profil''')

                self.TButton2_1 = ttk.Button(self.Labelframe2)
                self.TButton2_1.place(relx=0.368, rely=0.698, height=22, width=124
                        , bordermode='ignore')
                self.TButton2_1.configure(takefocus="")
                self.TButton2_1.configure(text='''Enrégistrer''')
                self.tooltip_font = "TkDefaultFont"
                self.TButton2_1_tooltip = \
                ToolTip(self.TButton2_1, self.tooltip_font, '''Enrégistrer les modifications effectuées ''')

                self.TButton2_2 = ttk.Button(self.Labelframe2)
                self.TButton2_2.place(relx=0.083, rely=0.698, height=22, width=124
                        , bordermode='ignore')
                self.TButton2_2.configure(takefocus="")
                self.TButton2_2.configure(text='''Supprimier''')
                self.tooltip_font = "TkDefaultFont"
                self.TButton2_2_tooltip = \
                ToolTip(self.TButton2_2, self.tooltip_font, '''Supprimer le contact de la liste''')

                self.TButton2_1_1 = ttk.Button(self.Labelframe2)
                self.TButton2_1_1.place(relx=0.367, rely=0.842, height=22, width=124
                        , bordermode='ignore')
                self.TButton2_1_1.configure(takefocus="")
                self.TButton2_1_1.configure(text='''Ajouter nouveau''')
                self.tooltip_font = "TkDefaultFont"
                self.TButton2_1_1_tooltip = \
                ToolTip(self.TButton2_1_1, self.tooltip_font, '''ajouter un nouveau contact''')