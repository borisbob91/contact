from interface.tkinker_import import *

from interface.support import *

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

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.013, rely=0.11, height=23, width=115)
        self.Label1.configure(font="-family {gothic} -size 14")
        self.Label1.configure(text='''Nom :''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.065, rely=0.262, height=23, width=115)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(font="-family {gothic} -size 14")
        self.Label1_1.configure(text='''Prénoms :''')

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.059, rely=0.387, height=23, width=115)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(cursor="fleur")
        self.Label1_2.configure(font="-family {gothic} -size 14")
        self.Label1_2.configure(text='''Numéro :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.326, rely=0.098, height=27, relwidth=0.535)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="-family {gothic} -size 12")

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

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.448, rely=0.866, height=25, width=140)
        self.Button1.configure(text='''Valider''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.087, rely=0.61, height=25, width=90)
        self.Button2.configure(cursor="fleur")
        self.Button2.configure(font="-family {gothic} -size 12")
        self.Button2.configure(text='''Photo''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.093, rely=0.872, height=25, width=110)
        self.Button3.configure(text='''Annuler''')
        self.Button3.configure(command= top.destroy)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.413, rely=0.518, height=85, width=159)
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(relief="ridge")
        self.Label2.configure(text='''Label''')


def pop_menu():
        pop = tk.Toplevel()

        pop_menu = PopMenu(pop)
        
if __name__ == '__main__':

    pop_menu()