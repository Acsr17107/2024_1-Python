from tkinter import *
str = ['파이썬', '코틀린']
win = Tk()
et1 = Entry(win, width = 20)
et1.grid(row = 0, column = 0, columnspan = 2)

def setstr(value):
    et1.delete(0, END)
    et1.insert(0, value)

py = Button(win, text=str[0], command = lambda: setstr(str[0]))
py.grid(row = 1, column = 0)
ko = Button(win, text=str[1], command = lambda: setstr(str[1]))
ko.grid(row = 1, column = 1)

win.mainloop()
