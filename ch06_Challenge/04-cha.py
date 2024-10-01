from random import choice
dcs = {'가위':'보오', '바위':'가위', '보오':'바위'}
tit = ['비김', '철수', '영희', '승자']
rsp = ('가위', '바위', '보오')

print('*'*20)
print('{:4} {:4} {:4}'.format(tit[1], tit[2], tit[3]))
print('*'*20)

a = 0
b = 0
c = 0

for _ in range(20):
    cs = choice(rsp)
    yh = choice(rsp)

    print('{:4} {:4}'.format(cs, yh), end=' ')

    if cs == yh:
        index = 0
        a += 1
    elif dcs[cs] == yh:
        index = 1
        b += 1
    else:
        index = 2
        c += 1
    print('{:4}'.format(tit[index]), end='')

    if cs == yh:
        print(a)
    elif dcs[cs] == yh:
        print(b)
    else:
        print(c)
print('총 게임 회수: 20 비긴 회수:', a)
print('철수 승률: {:.2f}'.format(b / (20 - a)))
print('영희 승률: {:.2f}'.format(c / (20 - a)))