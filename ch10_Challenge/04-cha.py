from tkinter import *
win = Tk()
win.title('반가워요, Tkinter!')
win.geometry('300x200')

def co():
    print('command: 안녕!')

def bi(event):
    print('bind: 안녕!')

btn = Button(win, text='인사 이벤트 처리', command = co)
btn.pack(expand=True, fill='both')
btn.bind("<Button-1>", bi)

win.mainloop()