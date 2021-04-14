import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class SessionGui:
    def __init__(self, top):

        self.session_frame = tk.LabelFrame(top)
        self.session_frame.place(relx=0.329, rely=0.015, relheight=0.128
                , relwidth=0.373)
        self.session_frame.configure(relief='groove', text='''Session Info''')

        self.user_id_label = tk.Label(self.session_frame)
        self.user_id_label.place(relx=0.029, rely=0.235, height=25, width=69
                , bordermode='ignore')
        self.user_id_label.configure(font="-family {gothic} -size 12")
        self.user_id_label.configure(relief="groove", text='''UserId:''')

        self.username_label = tk.Label(self.session_frame)
        self.username_label.place(relx=0.265, rely=0.235, height=25, width=129
                , bordermode='ignore')
        self.username_label.configure(activebackground="#f9f9f9")
        self.username_label.configure(font="-family {gothic} -size 12")
        self.username_label.configure(justify='left', relief="sunken")
        self.username_label.configure(text='''BorisBob''')

        self.logout_btn = tk.Button(self.session_frame)
        self.logout_btn.place(relx=0.029, rely=0.647, height=25, width=120
                , bordermode='ignore')
        self.logout_btn.configure(font="-family {gothic} -size 12")
        self.logout_btn.configure(text='''Deconnecter''')