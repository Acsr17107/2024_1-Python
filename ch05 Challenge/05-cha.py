sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]
print('메소드 insert()로 팀원 수 삽입')

for i in range(len(sports)):
    sports.insert(2 * i + 1, num[i])
print(sports)
print()
print("메소드 insert()로 '' 삽입")

for i in range(4):
    del sports[2 * i + 1]
    sports.insert(2 * i + 1, '')
print(sports)
print()
print('슬라이스 sports[1::2]에 num을 대입')

sports[1::2] = num
print(sports)