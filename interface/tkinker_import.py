
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

try:
    import Tkinter as tk
    import Tkinter

    from Tkinter import  messagebox
except ImportError:
    import tkinter as tk
    import tkinter

    from tkinter import  messagebox