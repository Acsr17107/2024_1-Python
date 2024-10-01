def togallon(liter):
    g = l * 0.264
    print('{:.2f} 리터 == {:.2f} 갤론'.format(l, g))

def toliter(gallon):
    l = g * 3.785
    print('{:.2f} 갤론 == {:.2f} 리터'.format(g, l))

a = int(input('번호 선택 1. 갤론 => 리터  2. 리터 => 갤론 >> '))

if a == 1:
    g = float(input('변환할 갤론은? '))
    toliter(g)
else:
    l = float(input('변환할 리터는? '))
    togallon(l)