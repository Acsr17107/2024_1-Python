from random import randint
f = randint(1, 100)
print('첫 값은', f, '이다')
while 1:
    a = input('산술 연산의 종류를 입력하세요. >> ')
    if '+' == a:
        b = int(input('두 번째 피연산자를 입력하세요. >> '))
        print(f, a, b, '=', f + b)
    elif '-' == a:
        b = int(input('두 번째 피연산자를 입력하세요. >> '))
        print(f, a, b, '=', f - b)
    elif '*' == a:
        b = int(input('두 번째 피연산자를 입력하세요. >> '))
        print(f, a, b, '=', f * b)
    elif '/' == a:
        b = int(input('두 번째 피연산자를 입력하세요. >> '))
        print(f, a, b, '=', f / b)
    elif '%' == a:
        b = int(input('두 번째 피연산자를 입력하세요. >> '))
        print(f, a, b, '=', f % b)
    else:
        break
print(' 종료 '.center(32, '*'))