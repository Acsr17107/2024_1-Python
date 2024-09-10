from random import randint, choice
import turtle as t

tshs = ['arrow', 'circle', 'turtle', 'square', 'triangle', 'classic']
han = ['화살', '원', '거북이', '사각형', '삼각형', '전통']
cols = ['red', 'blue', 'green', 'purple', 'magenta', 'black', 
        'gray', 'yellow', 'cyan', 'orange', 'aqua']

t.setup(800, 500)
t.speed(0)

for i in range(20):
    t.shape(tshs[i % len(tshs)])
    t.color(choice(cols))
    x = randint(-300, 300)
    y = randint(-200, 200)
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cols[i % len(cols)])
    t.begin_fill()
    t.circle(randint(3, 50))
    t.end_fill()

    t.write(han[i % len(han)])