from random import randint
while 1:
    a = randint(1, 99)
    b = randint(1, 99)
    print('{0} * {1} = {2}'.format(a, b, a * b))
    print()
    c = input('계속 y / n ? ')
    if 'y' == c:
        continue
    elif 'n' == c:
        break