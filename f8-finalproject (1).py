from tkinter import *

window = Tk()
window.title("Tax Calculator")
window.config(bg="#60A3D9")
window.geometry("795x675+20+10")


class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Tax Calculator PH 2022", font="Arial 20 bold", bg="#60A3D9")
        self.lbl1.place(relx=0.5, y=40, anchor="center")

        self.c1 = Canvas(window, width=345, height=90, relief="ridge", bd=3)
        self.c1.place(x=225, y=75)
        self.lbl2 = Label(window, text="Monthly Income:", font="Arial 12 bold")
        self.lbl2.place(x=250, y=85)
        self.txt2 = Entry(window, bd=3, font="bold")
        self.txt2.place(x=400, y=100, anchor="w", height=30, width=150)

        self.btn1 = Button(window, text="Calculate", command=self.calc, font="Bold 12", bg="#ADDFFF")
        self.btn1.place(x=350, y=140, anchor="center")
        self.btn1.config(height=1)

        self.btn2 = Button(window, text="Clear", anchor="center", command=self.clear, font="Bold 12", bg="#ADDFFF")
        self.btn2.place(x=440, y=140, anchor="center")
        self.btn2.config(height=1)

        self.c2 = Canvas(window, width=320, height=270, relief="ridge", bd=3)
        self.c2.place(x=50, y=200)
        self.c2lbl1 = Label(window, text="Tax Computation", font="Arial 17")
        self.c2lbl1.place(x=130, y=205)
        self.lbl4 = Label(window, text="Income Tax:", font="Arial 15")
        self.lbl4.place(x=75, y=270)
        self.txt4 = Entry(window, bd=3, font="bold")
        self.txt4.config(state="readonly")
        self.txt4.place(x=190, y=270, height=35, width=150)

        self.lbl5 = Label(window, text="Net Pay", font="Arial 15")
        self.lbl5.place(x=75, y=320)
        self.lbl5a = Label(window, text="After Tax:", font="Arial 15")
        self.lbl5a.place(x=75, y=345)
        self.txt5 = Entry(window, bd=3, font="bold")
        self.txt5.config(state="readonly")
        self.txt5.place(x=190, y=330, height=35, width=150)

        self.c3 = Canvas(window, width=320, height=270, relief="ridge", bd=3)
        self.c3.place(x=420, y=200)
        self.c3lbl1 = Label(window, text="Contribution", font="Arial 17")
        self.c3lbl1.place(x=523, y=205)

        self.lbl6 = Label(window, text="SSS:", font="Arial 13")
        self.lbl6.place(x=450, y=250)
        self.txt6 = Entry(window, bd=3, font="bold")
        self.txt6.config(state="readonly")
        self.txt6.place(x=550, y=245, height=35, width=150)

        self.lbl7 = Label(window, text="PAG-IBIG:", font="Arial 13")
        self.lbl7.place(x=450, y=295)
        self.txt7 = Entry(window, bd=3, font="bold")
        self.txt7.config(state="readonly")
        self.txt7.place(x=550, y=290, height=35, width=150)

        self.lbl8 = Label(window, text="PhilHealth:", font="Arial 13")
        self.lbl8.place(x=450, y=340)
        self.txt8 = Entry(window, bd=3, font="bold")
        self.txt8.config(state="readonly")
        self.txt8.place(x=550, y=335, height=35, width=150)

        self.lbl9 = Label(window, text="Total Contribution:", font="Arial 13 bold")
        self.lbl9.place(x=500, y=380)
        self.txt9 = Entry(window, bd=3, font="bold", justify="center")
        self.txt9.config(state="readonly")
        self.txt9.place(x=475, y=410, height=35, width=200)

        self.c4 = Canvas(window, width=690, height=120, relief="ridge", bd=3)
        self.c4.place(x=50, y=505)

        self.lbl10 = Label(window, text="Total Deductions:", font="Arial 14")
        self.lbl10.place(x=225, y=530)
        self.txt10 = Entry(window, bd=3, font="bold")
        self.txt10.config(state="readonly")
        self.txt10.place(x=390, y=525, height=35, width=150)

        self.lbl11 = Label(window, text="Net Pay After Deduction:", font="Arial 14")
        self.lbl11.place(x=165, y=580)
        self.txt11 = Entry(window, bd=3, font="bold")
        self.txt11.config(state="readonly")
        self.txt11.place(x=390, y=575, height=35, width=150)

    def calc(self):
        # income tax= taxable income x look at table
        # Taxable Income = (Monthly Basic Pay + Additional Pay) – (total contribution)

        # income tax
        self.txt4.config(state="normal")
        self.txt4.delete(0, 'end')
        m_income = float(self.txt2.get())
        totalcontribution = (m_income * .04) + (m_income * .02) + (m_income * .04)
        taxableincome = m_income - totalcontribution
        if taxableincome <= 0:
            result = 0
        elif taxableincome < 20833:
            result = taxableincome * .0
        elif taxableincome > 20833 or taxableincome <= 33332:
            result = (taxableincome - 20833) * .20
        elif taxableincome >= 33333 or taxableincome <= 66666:
            result = (2500 + ((taxableincome - 33333) * .25))
        elif taxableincome >= 66667 or taxableincome <= 166666:
            result = (10833.33 + ((taxableincome - 66667) * .30))
        elif taxableincome >= 166667 or taxableincome <= 666666:
            result = (40833.33 + ((taxableincome - 166, 667) * .32))
        elif taxableincome >= 666667:
            result = (200833.33 + ((taxableincome - 666667) * .35))
        self.txt4.insert(END, str(round(result, 2)))
        self.txt4.config(state="readonly")

        # net pay
        self.txt5.config(state="normal")
        self.txt5.delete(0, 'end')
        m_income = float(self.txt2.get())
        incometax = float(self.txt4.get())
        if m_income < 0:
            result = 0
        else:
            result = m_income - incometax
        self.txt5.insert(END, str(round(result, 2)))
        self.txt5.config(state="readonly")

        # SSS
        self.txt6.config(state="normal")
        self.txt6.delete(0, 'end')
        m_income = float(self.txt2.get())
        if m_income <= 0:
            result = 0
        elif m_income:
            result = (m_income * .04)
        self.txt6.insert(END, str(round(result, 2)))
        self.txt6.config(state="readonly")

        # Pagibig
        self.txt7.config(state="normal")
        self.txt7.delete(0, 'end')
        m_income = float(self.txt2.get())
        if m_income <= 0:
            result = 0
        elif m_income <= 1500:
            result = (m_income * .01)
        elif m_income:
            result = (m_income * .02)
        self.txt7.insert(END, str(round(result, 2)))
        self.txt7.config(state="readonly")

        # Philhealth
        self.txt8.config(state="normal")
        self.txt8.delete(0, 'end')
        m_income = float(self.txt2.get())
        if m_income <= 0:
            result = 0
        elif m_income:
            result = (m_income * .04)
        self.txt8.insert(END, str(round(result, 2)))
        self.txt8.config(state="readonly")

        # totalcontribution
        self.txt9.config(state="normal")
        self.txt9.delete(0, 'end')
        m_income = float(self.txt2.get())
        if m_income <= 0:
            result = 0
        elif m_income <= 1500:
            result = (m_income * .04) + (m_income * .01) + (m_income * .04)
        elif m_income:
            result = (m_income * .04) + (m_income * .02) + (m_income * .04)
        self.txt9.insert(END, str(round(result, 2)))
        self.txt9.config(state="readonly")

        # total deductions = income tax + total contribution
        self.txt10.config(state="normal")
        self.txt10.delete(0, 'end')
        incometax = float(self.txt4.get())
        totalcontri = float(self.txt9.get())

        result = totalcontri + incometax
        self.txt10.insert(END, str(round(result, 2)))
        self.txt10.config(state="readonly")

        # net pay after deductions
        self.txt11.config(state="normal")
        self.txt11.delete(0, 'end')
        m_income = float(self.txt2.get())
        totaldeduc = float(self.txt10.get())
        if m_income < 0:
            result = 0
        else:
            result = m_income - totaldeduc
        self.txt11.insert(END, str(round(result, 2)))
        self.txt11.config(state="readonly")

    def clear(self):
        self.txt4.config(state="normal")
        self.txt5.config(state="normal")
        self.txt6.config(state="normal")
        self.txt7.config(state="normal")
        self.txt8.config(state="normal")
        self.txt9.config(state="normal")
        self.txt10.config(state="normal")
        self.txt11.config(state="normal")

        self.txt2.delete(0, END)
        self.txt4.delete(0, 'end')
        self.txt5.delete(0, 'end')
        self.txt6.delete(0, 'end')
        self.txt7.delete(0, 'end')
        self.txt8.delete(0, 'end')
        self.txt9.delete(0, 'end')
        self.txt10.delete(0, 'end')
        self.txt11.delete(0, 'end')

        self.txt4.config(state="readonly")
        self.txt5.config(state="readonly")
        self.txt6.config(state="readonly")
        self.txt7.config(state="readonly")
        self.txt8.config(state="readonly")
        self.txt9.config(state="readonly")
        self.txt10.config(state="readonly")
        self.txt11.config(state="readonly")


mywin = MyWindow(window)

window.mainloop()
