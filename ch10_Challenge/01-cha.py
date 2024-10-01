from tkinter import *
rtype = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']
win = Tk()
win.geometry('300x130')
win.title('레이블의 다양한 모습')


for t in rtype:
    lb = Label(win, relief=t, text=t)
    lb.pack()

win.mainloop()