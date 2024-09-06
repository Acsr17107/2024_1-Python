a = int(input('소수(prime number)인지를 판별한 2 이상의 정수 입력 >> '))
c = 0
for i in range(1, a+1):
    if a % i == 0:
        c += 1
if c == 2:
    print('정수 {0}는 소수이다.'.format(a))
else:
    print('정수 {0}는 소수가 아니다.'.format(a))