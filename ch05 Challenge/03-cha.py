print('+ 012345678901')
print(' HelloPython!')
print('- 210987654321')
lst = list('HelloPython!')
while 1:
    a, b, c = map(int, input('슬라이스[?:?:?] 3개 입력 >> ').split())
    if a == b == c == 0:
        print('종료'.center(30, '*'))
        break
    else:
        print(lst[a:b:c])