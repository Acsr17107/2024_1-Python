from random import sample
from random import randint

# 로또 복권 순위 판정에 사용할 딕셔너리
rank = { 6: ('1등', 1000000000), # 1등 10억 원, 멎춘 번호 6개
         5: {1: ('2등', 50000000), # 2등 5천만 원, 맞춘 번호 5개 + 보너스
             0: ('3등', 1000000)}, # 3등 1백만 원, 맞춘 번호 5개
         4: ('4등', 50000), # 4등 5만 원, 맞춘 번호 4개
         3: ('5등', 5000) # 5등 5천원, 맞춘 번호 3개
       }

def makenum(same):
    nums = winnum.copy()
    # 다르게 만들기 위해 제거 6-same개 제거
    for i in range(6 - same):
        nums.pop()

    # 당첨 번호가 아닌 2개를 넣어 모두 6개 만들기
    while len(nums) != 6:
        n = randint(1, 45)
        if n not in winnum:
            nums.add(n)
    return nums

def getwinner(lotto):
    ''' 6개의 로또 번호에서 각각 당첨 번호 개수와 수를 출력 '''
    global bonus
    for i, item in enumerate(lotto):
        print('%c' % (ord('A') + i), end = ' ')
        win = winnum.intersection(item) # 당첨 번호 구하기
        if win:
            wincnt = len(win)
            print('당첨 번호 개수 %d, ' % wincnt, end = '')
            printnums(win)
            if 3 <= wincnt:
                grade = rank[wincnt]
                if 5 == wincnt:
                    if bonus in item:
                        print('\t 보너스 번호 %d도 맞춤!!!' % bonus)
                        grade = rank[wincnt][1] # 2등 지정
                    else:
                        grade = rank[wincnt][0] # 3등 지정
                print('\t%s %s원' % (grade[0], grade[1]))
            else:
                print('\t 2개 이하 맞춰, 꽝!')
        else:
            print('모두 꽝!!!')

def printlotto(lotto):
    ''' 로또 복권 표와 같이 출력 '''
    for i, item in enumerate(lotto):
        print('%c 자동 ' % (ord('A') + i), end = ' ')
        printnums(item)
    print()

def printnums(nums):
    ''' 시퀀스인 수를 정렬해 출력 '''
    for num in sorted(nums):
        print('%02d' % num, end = ' ')
    print()

# 7개 선정
winnum = set(sample( list(range(1, 46)), 7))
# 1개를 빼 보너스 번호로 사용
bonus = winnum.pop()

print('당첨 번호: ', end = '')
printnums(winnum) # 당첨 번호 출력
print('보너스 번호:', bonus)
print()

lottos = []
# 1등 번호(6개 모두 같은 셋)를 만들어 로또 리스트에 추가
rank1num = winnum.copy()
lottos.append(rank1num)

# 2등 번호(5개 같고, 1개는 보너스 번호)를 만들어 로또 리스트에 추가
rank2num = winnum.copy()
rank2num.pop(); rank2num.add(bonus)
lottos.append(rank2num)

# 3등 번호(5개 같고, 1개는 보너스 번호와 다르게)를 만들어 로또 리스트에 추가
rank3num = winnum.copy()
rank3num.pop()
# 보너스 번호가 아니고 기존의 번호가 아니면 1개 추가
while True:
    num = randint(1, 45)
    if num != bonus and num not in rank3num:
        rank3num.add(num)
        break
lottos.append(rank3num)

# 4개부터 0개 맞는 번호 자동 생성
for i in range(5):
    lottos.append(makenum(4 - i))

# 로또 번호 출력
printlotto(lottos)
# 로또 번호와 당첨번호 비교해 순위 결정 출력
getwinner(lottos)