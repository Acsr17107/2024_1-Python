from tkinter import *
rtype = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']
win = Tk()
win.geometry()
win.title('그리드에 배치한 버튼의 다양한 모습')

for i, t in enumerate(rtype):
    if i%2 == 0:
        btn = Button(win, text='({}, {})'.format(i//2, 0), relief=t, width=30)
        btn.grid(row = i//2, column = 0)
    else:
        btn = Button(win, text='({}, {})'.format((i - 1)//2, 1), relief=t, width=30)
        btn.grid(row = (i - 1)//2, column = 1)

win.mainloop()