from interface.tkinker_import  import *
import sys
import platform
import time

class PopProgressGui:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("350x50+597+388")
        top.minsize(1, 1)
        top.maxsize(1585, 870)
        top.resizable(1,  1)
        top.title("Traitement encours")
        global progress_var
        progress_var = "0.0"
        progress_var = tk.IntVar()
        self.progress_var = tk.IntVar()
        
        self.Pop_progress = ttk.Progressbar(top)
        self.Pop_progress.place(relx=0.091, rely=0.4, relwidth=0.8, relheight=0.0
                , height=19)
        self.Pop_progress.configure(length="280")
        self.Pop_progress.configure(variable=progress_var)
        self.Pop_progress.configure(value="0.0")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.377, rely=0.02, height=14, width=99)
        self.Label1.configure(font="-family {gothic} -size 11")
        self.Label1.configure(text=''' 100 %''')
    def progress_size(self, size=0.5):
        global progress_var
        progress_var.set(size*100)

    def update_size(self, size=0.2):
        pass

def set_Tk_var():
    pass

progress_app = None
pop_window = None

def progress_launcher(size=0.8, *args, **kargs):
    #progress_destroy()
    global progress_app 
    progress_app = tk.Toplevel()
    global pop_window
    pop_window = PopProgressGui(progress_app)
    pop_window.progress_size(size)
    
    

def set_size(size=0.5):
    PopProgressGui.progress_size(size*100)

def progress_destroy():
    if progress_app:
        progress_app.destroy()
        pop_window = None

if __name__ == '__main__':
    progress_launcher()