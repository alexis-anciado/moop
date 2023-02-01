from tkinter import *
from tkinter import ttk

window = Tk()
window.title("TASK MANAGEMENT SYSTEM")
window.geometry("400x400")
window.configure(background="darkcyan", bd=20, relief=FLAT)
window.resizable(False, False)
tasklist = []

class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, background="dark cyan", font="Seaford 10 bold", text="INSERT NEW TASK")
        self.lbl1.place(x=0, y=0, anchor="nw")

        self.txt1 = Entry(window, background="light cyan", bd=3, width=48)
        self.txt1.place(x=0, y=20, anchor="nw")

        self.btn1 = Button(window, background="cyan3", relief=RAISED, font="Seaford 8 bold", text="ADD TASK", command=self.addtask)
        self.btn1.place(x=300, y=20)

        self.lbl2 = Label(window, background="dark cyan", font="Seaford 10 bold", text="LIST OF UNFINISHED TASKS")
        self.lbl2.place(x=180, y=70, anchor="center")

        self.lbx1 = Listbox(window, background="light cyan", bd=3, width=59, state=DISABLED)
        self.lbx1.place(x=0, y=80, anchor="nw", height=200)

        self.lbl4 = Label(window, background="dark cyan", font="Seaford 10 bold", text="WHICH TASK HAVE YOU FINISHED?")
        self.lbl4.place(x=0, y=300, anchor="nw")

        self.btn2 = Button(window, background="cyan3", relief=RAISED, font="Seaford 8 bold", text="REMOVE TASK", command=self.removetask)
        self.btn2.place(x=277, y=325)

        self.lcb1 = ttk.Combobox(window, font="Seaford 8 bold", width=40, values=[])
        self.lcb1.grid(column=1, row=5)
        self.lcb1.place(x=0, y=325, anchor="nw")

        self.lbl3 = Label(window, background="dark cyan", font="Seaford 8 bold", text="")
        self.lbl3.place(x=180, y=53, anchor="center")

    def addtask(self):
        task = str(self.txt1.get())

        if task and not task.isspace():
            self.lbl3.config(text="")
        else:
            self.lbl3.config(text="Please input a task.")
            return

        self.lbx1.configure(state=NORMAL)
        self.lbx1.insert(END, " • " + str(task))
        tasklist.append(task)
        self.lcb1.config(values=tasklist)
        self.txt1.delete(0, END)
        self.lbx1.configure(state=DISABLED)


    def removetask(self):
        task = self.lcb1.get()
        self.lbx1.configure(state=NORMAL)
        self.lbx1.delete(tasklist.index(task))
        tasklist.remove(task)
        self.lcb1.config(values=tasklist)
        self.lcb1.delete(0, 'end')
        self.lbx1.configure(state=DISABLED)


MyWin = MyWindow(window)
window.mainloop()

#https://tkdocs.com/tutorial/widgets.html