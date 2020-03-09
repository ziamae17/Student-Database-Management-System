import getpass
import sys
import tkinter
import tkinter.messagebox

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

#import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    #unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    #unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def cancelLogin(self):
        msg=tkinter.messagebox.askyesno("Student Database Management System", "Are you sure you want to cancel login?");
        if (msg):
            exit()

    def loginUser(self):
        name=self.Entry1.get()
        passwd=self.Entry1_4.get()

        if name == "admin" and passwd == "@dm1n":
                tkinter.messagebox.showinfo("Student Database Management System", "Access Granted!");
                import main.py
        else:
                tkinter.messagebox.showwarning("Student Database Management System", "The Username or Password is Incorrect!");

    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Black} -size 10 -weight bold"
        font11 = "-family {Segoe UI} -size 10 -weight bold"
        font13 = "-family {Segoe UI} -size 9"
        font9 = "-family {Segoe UI} -size 23"

        top.geometry("389x320+413+194")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Student Database Management System")
        top.configure(background="#e2e2e2")
        top.configure(highlightbackground="#252525")
        top.configure(highlightcolor="#252525")

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.172, rely=0.241, height=49, width=64)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#e2e2e2")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font10)
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''User ID:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.188, rely=0.363,height=20, relwidth=0.627)
        self.Entry1.configure(background="#f2f2f2")
        self.Entry1.configure(disabledforeground="#676767")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#000000")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(readonlybackground="#f7eff8")
        self.Entry1.configure(selectbackground="#000000")
        self.Entry1.configure(selectforeground="#000000")

        self.Label2_3 = tk.Label(top)
        self.Label2_3.place(relx=0.141, rely=0.441, height=29, width=99)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#e2e2e2")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font11)
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Password:''')

        self.Entry1_4 = tk.Entry(top)
        self.Entry1_4.place(relx=0.185, rely=0.528,height=20, relwidth=0.627)
        self.Entry1_4.configure(background="#f2f2f2")
        self.Entry1_4.configure(disabledforeground="#252525")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="#c4c4c4")
        self.Entry1_4.configure(selectforeground="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#cfd0e2',fg='#3e3e3e')
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.18, rely=0.719, height=24, width=77)
        self.Button1.configure(activebackground="#252525")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Cancel''')
        self.Button1.configure(command=self.cancelLogin);

        self.Button1_5 = tk.Button(top)
        self.Button1_5.place(relx=0.617, rely=0.719, height=24, width=77)
        self.Button1_5.configure(activebackground="#ececec")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#d9d9d9")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(font=font13)
        self.Button1_5.configure(foreground="#000000")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(text='''Login''')
        self.Button1_5.configure(command=self.loginUser);

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.308, rely=0.063, height=51, width=144)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#e2e2e2")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Log In''')

if __name__ == '__main__':
    vp_start_gui()





