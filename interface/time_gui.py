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

class TimeGui:
    def __init__(self, top):
        self.time_frame = tk.Frame(top)
        self.time_frame.place(relx=0.746, rely=0.024, relheight=0.113
                , relwidth=0.237)
        self.time_frame.configure(relief='groove', borderwidth="2")

        self.date_label = tk.Label(self.time_frame)
        self.date_label.place(relx=0.245, rely=0.107, height=25, width=129)
        self.date_label.configure(font="-family {gothic} -size 12")
        self.date_label.configure(text='''13/04/2021''')

        self.time_label = tk.Label(self.time_frame)
        self.time_label.place(relx=0.25, rely=0.413, height=35, width=129)
        self.time_label.configure(activebackground="#f9f9f9")
        self.time_label.configure(font="-family {gothic} -size 14")
        self.time_label.configure(text='''21:58:21''')