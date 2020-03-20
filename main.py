import csv
import sys
import tkinter
import tkinter.messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

    
class studentsProf():
    def __init__(self,ID,FirstName,LastName,Course,YearLevel):
        self.ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Course = Course
        self.YearLevel = YearLevel
        

class data():

    def __init__(self):
        self.students = []
        self.list_students = []
        self.index=0
        self.read_from_file()
        self.list_students = [*self.students]

    def read_from_file(self):
        with open('Students.csv',newline='') as inf:
            info=csv.reader(inf,delimiter=',')
            for row in info:
                self.students.append(studentsProf(row[0],row[1],row[2],row[3],row[4]))
            print(self.students)

    def write_to_file(self):
        with open('Students.csv','w',newline='') as data:
            result=csv.writer(data,delimiter=',')
            for a in self.students:
                result.writerow([a.ID]+[a.FirstName]+[a.LastName]+[a.Course]+[a.YearLevel])
        
                

def vp_start_gui():
    global val, w, root, top
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = tk.Toplevel (root)

class Toplevel1:
       
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1054x469+150+131")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Welcome to Student Database Management System")
        top.configure(background="#e2e2e2")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top,command=lambda: CREATE(self.Entry1.get(),self.Entry2.get(),self.Entry3.get(),self.Entry4.get(),self.Entry5.get()))
        self.Button1.place(relx=0.361, rely=0.448, height=34, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Student''')
        
        self.Button2 = tk.Button(top)
        """
        self.Button2.place(relx=0.361, rely=0.533, height=34, width=117)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''View All Students''')"""

        self.Button3 = tk.Button(top,command=update)
        self.Button3.place(relx=0.361, rely=0.618, height=34, width=117)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Update Student Info''')

        self.Button4 = tk.Button(top,command=delete)
        self.Button4.place(relx=0.361, rely=0.704, height=34, width=117)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Delete Student''')

        self.Button5 = tk.Button(top, command=root.destroy)
        self.Button5.place(relx=0.361, rely=0.789, height=34, width=117)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Exit''')
        

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.02, rely=0.384, height=25, width=108)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#e2e2e2")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ID No :''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.448, height=25, width=115)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#e2e2e2")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''First Name :''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.001, rely=0.512, height=25, width=115)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#e2e2e2")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Last Name :''')
        """
        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.047, rely=0.576, height=25, width=68)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#e2e2e2")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Sex :''')"""

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.013, rely=0.64, height=25, width=115)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#e2e2e2")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 12")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Course :''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.0, rely=0.704, height=25, width=113)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#e2e2e2")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 12")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Year Level :''')

        #ID
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.104, rely=0.386,height=20, relwidth=0.089)
        self.Entry1.configure(background="#f2f2f2")
        self.Entry1.configure(disabledbackground="#f0f0f0f0f0f0")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#00182d")
        self.Entry1.configure(selectforeground="black")

        #fname
        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.104, rely=0.45,height=20, relwidth=0.203)
        self.Entry2.configure(background="#f2f2f2")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.152, rely=0.064, relheight=0.203
                , relwidth=0.707)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.199, rely=0.085, height=71, width=645)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Student Database Management System''')

        #Lname
        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.104, rely=0.514,height=20, relwidth=0.203)
        self.Entry3.configure(background="#f2f2f2")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        """
        self.Checkbutton1 = tk.Checkbutton(top)
        self.Checkbutton1.place(relx=0.104, rely=0.576, relheight=0.053
                , relwidth=0.058)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#e2e2e2")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 10")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Male''')
        self.Checkbutton1.configure(variable=GUI_support.che86)

        self.Checkbutton2 = tk.Checkbutton(top)
        self.Checkbutton2.place(relx=0.166, rely=0.576, relheight=0.053
                , relwidth=0.065)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#e2e2e2")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font="-family {Segoe UI} -size 10")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Female''')
        self.Checkbutton2.configure(variable=GUI_support.che87)"""

        #Course
        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.104, rely=0.642,height=20, relwidth=0.203)
        self.Entry4.configure(background="#f2f2f2")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        #Year Level
        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.104, rely=0.706,height=20, relwidth=0.203)
        self.Entry5.configure(background="#f2f2f2")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.484, rely=0.448, relheight=0.416
                , relwidth=0.501)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        #Search
        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.56, rely=0.388,height=20, relwidth=0.118)
        self.Entry6.configure(background="#f2f2f2")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")
        self.Entry6.bind('<KeyRelease>',search)

        """
        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.361, rely=0.362, height=34, width=117)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Search Student''')"""

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.479, rely=0.392, height=21, width=86)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#e2e2e2")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 12")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Enter ID No. :''')

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.484, rely=0.448, relheight=0.431
                , relwidth=0.501)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.bind('<<ListboxSelect>>',select)
        for i in Csv.list_students:
            self.Listbox1.insert("end", i.ID+" | "+i.FirstName+" | "+i.LastName+" | "+i.Course+" | "+i.YearLevel)
        self.scrollbar = tk.Scrollbar(top)
        self.scrollbar.place(relx=0.98, rely=0.448, relheight=0.431
                , relwidth=0.01)
        self.Listbox1.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.Listbox1.yview)
        
        


    @staticmethod
    def popup1(event):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Segoe UI} -size 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event):
        Popupmenu2 = tk.Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="-family {Segoe UI} -size 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)

    @staticmethod
    def popup3(event):
        Popupmenu3 = tk.Menu(root, tearoff=0)
        Popupmenu3.configure(activebackground="#f9f9f9")
        Popupmenu3.configure(activeborderwidth="1")
        Popupmenu3.configure(activeforeground="black")
        Popupmenu3.configure(background="#d9d9d9")
        Popupmenu3.configure(borderwidth="1")
        Popupmenu3.configure(disabledforeground="#a3a3a3")
        Popupmenu3.configure(font="-family {Segoe UI} -size 9")
        Popupmenu3.configure(foreground="black")
        Popupmenu3.post(event.x_root, event.y_root)

    @staticmethod
    def popup4(event):
        Popupmenu4 = tk.Menu(root, tearoff=0)
        Popupmenu4.configure(activebackground="#f9f9f9")
        Popupmenu4.configure(activeborderwidth="1")
        Popupmenu4.configure(activeforeground="black")
        Popupmenu4.configure(background="#d9d9d9")
        Popupmenu4.configure(borderwidth="1")
        Popupmenu4.configure(disabledforeground="#a3a3a3")
        Popupmenu4.configure(font="-family {Segoe UI} -size 9")
        Popupmenu4.configure(foreground="black")
        Popupmenu4.post(event.x_root, event.y_root)

    @staticmethod
    def popup5(event):
        Popupmenu5 = tk.Menu(root, tearoff=0)
        Popupmenu5.configure(activebackground="#f9f9f9")
        Popupmenu5.configure(activeborderwidth="1")
        Popupmenu5.configure(activeforeground="black")
        Popupmenu5.configure(background="#d9d9d9")
        Popupmenu5.configure(borderwidth="1")
        Popupmenu5.configure(disabledforeground="#a3a3a3")
        Popupmenu5.configure(font="-family {Segoe UI} -size 9")
        Popupmenu5.configure(foreground="black")
        Popupmenu5.post(event.x_root, event.y_root)

def refresh():
    root.destroy()
    vp_start_gui()
def CREATE(a,b,c,d,e):
    Csv.students.append(studentsProf(a,b,c,d,e))
    Csv.write_to_file()
    refresh()
def select(event):
    Csv.index = top.Listbox1.curselection()
    Csv.index=Csv.index[0]
    #index = top.Listbox1.get(top.Listbox1.curselection(),top.Listbox1.curselection())
def delete():
    Csv.students.remove(Csv.list_students[Csv.index])
    Csv.list_students.pop(Csv.index)
    Csv.write_to_file()
    refresh()
def update():
    #top.Button2 = tk.Button(top,command=confirm)
    top.Button2.place(relx=0.361, rely=0.533, height=34, width=117)
    top.Button2.configure(activebackground="#ececec")
    top.Button2.configure(activeforeground="#000000")
    top.Button2.configure(background="#d9d9d9")
    top.Button2.configure(disabledforeground="#a3a3a3")
    top.Button2.configure(foreground="#000000")
    top.Button2.configure(highlightbackground="#d9d9d9")
    top.Button2.configure(highlightcolor="black")
    top.Button2.configure(pady="0")
    top.Button2.configure(text='''Confirm''')
    top.Button2.configure(command=confirm)
    top.Button3.configure(text='''Cancel''')
    top.Button3.configure(command=refresh)
    top.Entry1.insert(0,Csv.list_students[Csv.index].ID)
    top.Entry2.insert(0,Csv.list_students[Csv.index].FirstName)
    top.Entry3.insert(0,Csv.list_students[Csv.index].LastName)
    top.Entry4.insert(0,Csv.list_students[Csv.index].Course)
    top.Entry5.insert(0,Csv.list_students[Csv.index].YearLevel)

def confirm():
    Csv.list_students[Csv.index].ID = top.Entry1.get()
    Csv.list_students[Csv.index].FirstName = top.Entry2.get()
    Csv.list_students[Csv.index].LastName = top.Entry3.get()
    Csv.list_students[Csv.index].Course = top.Entry4.get()
    Csv.list_students[Csv.index].YearLevel = top.Entry5.get()
    Csv.write_to_file()
    refresh()

def search(event):
    scan = top.Entry6.get()
    if len(scan)==0:
        Csv.list_students=[*Csv.students]
    else:
        temp=[]
        for i in Csv.students:
            if scan in i.ID:
                temp.append(i)
        Csv.list_students = [*temp]
    top.Listbox1.delete(0,'end')
    for i in Csv.list_students:
            top.Listbox1.insert("end", i.ID+" "+i.FirstName+" "+i.LastName+" "+i.Course+" "+i.YearLevel)
    
Csv = data()
vp_start_gui()




