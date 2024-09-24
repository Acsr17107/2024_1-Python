dates = int(input('한 달 최대 일수를 입력 >> '))
day = int(input('첫 날 1일의 시작 요일을 입력(0=일, 1=월, ... 6=토) >> '))
day %= 7 # 7이 넘어가면 재설정

# 요일 출력
print('\n', end= ' ')
for i in '일월화수목금토':
    print('%s' % i, end= ' ')
else:
    print('\n')

cnt = 0
# 빈 날짜 출력
if day != 0:
    print('   ' * day, end = '')
    cnt += day

# 1일부터 말일까지 출력
for i in range(1, dates + 1):
    print('%2d' % i, end= ' ')
    cnt += 1
    if cnt % 7 == 0: # 1주가 모두 출력되면 다음부터는 다음 줄에서 출력
        print()
else:
    print()