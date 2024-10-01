c = 20
while c < 42:
    f = c * 9/5 + 32
    F = c * 2 + 30
    abs = F - f
    print('섭씨:', c, '화씨:', f, '화씨(약식):', F, '차이: {:.2f}'.format(abs))
    c += 3