def getintrest(m, r, y):
    a = m * (1 + r) ** y
    print('{}년 총액: {:.2f}'.format(y, a))

print('예금 원금:', 300000)
getintrest(300000, 0.05, 2)
getintrest(300000, 0.05, 4)
getintrest(300000, 0.05, 6)
getintrest(300000, 0.05, 8)