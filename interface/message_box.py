from interface.tkinker_import import *

#messagbow : showerror, showinfo, showwarning, askyesno, askokcancel ...etc
title='code erreur:'
msg="veuillez un un msg"
def show_warming(title = title, msg=msg):
    messagebox.showwarning(title, msg)

def show_error(title = title, msg=msg):
	messagebox.showerror(title, msg)

def show_info(title = title, msg=msg):
	messagebox.showinfo(title, msg)

def show_yes_no(title = title, msg=msg):
	response = messagebox.askyesno(title,msg)
	return response


def show_question(title = title, msg=msg):
	response = messagebox.askquestion(title, msg)
	return response

def show_cancel_yes_no(title = title, msg = msg):
	response = messagebox.askyesnocancel(title, msg)
	return response

def show_ok_cancel(title= title, msg = msg):
	response = messagebox.askokcancel(title, msg)
	return response