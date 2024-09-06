for i in range(-7, 1):
    mask = 0xff
    print('10진수: {0:2d} 2진수: {1:8b} 8진수: {1:3o} 16진수: {1:2x}'.format(i, i&mask))