from random import randint
c = []

for i in range(9):
    a = randint(1, 100)
    c.append(a)

f = list(map(lambda c: c * 9/5 + 32, (c)))

print('섭씨 온도:', c)
print('화씨 온도:', f)

for c, f in zip(c, f):
    print('섭씨 온도 {} => 화씨 {}'.format(c, f))