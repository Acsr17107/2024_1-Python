from random import randint
c = 0
while c < 5:
    c += 1
    t = randint(35, 50)
    if t < 40:
        print('근로 시간', str(t) + '시간, 주급', 12000 * t)
    elif t >= 40:
        print('근로 시간', str(t) + '시간, 주급', int(12000 * 40 + (t - 40) * 12000 * 3 / 2))