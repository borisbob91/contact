from interface.tkinker_import import *

from .tooltip import ToolTip

class SearchGui:
    def __init__(self, top):
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
        self.search_radio_btn.configure(variable='')
        self.search_radio_btn.configure(value = 0)

        self.search_radio_btn_1 = tk.Radiobutton(self.search_frame)
        self.search_radio_btn_1.place(relx=0.068, rely=0.471, relheight=0.2131, relwidth=0.37)
        self.search_radio_btn_1.configure(justify='left')
        self.search_radio_btn_1.configure(text='''Par Numero''')
        self.search_radio_btn_1.configure(variable='')
        self.search_radio_btn_1.configure(value = 1)

          #messagbow : showerror, showinfo, showwarning, askyesno, askokcancel ...etc
    def show_message_box(self):
        messagebox.showwarning('Attentions:', "Veuillez entrez une valeur")

    def get_search_value(self):
        value_enter = self.search_Entry.get()
        
        if not value_enter:
            self.show_message_box()
        else:
            messagebox.showinfo('Info:', "recherche validée ! ")