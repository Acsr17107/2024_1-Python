from random import randint
lst = []
for i in range(10):
    a = randint(1, 99)
    lst.append(a)
print('리스트: ', lst)
t = tuple(lst)
print('튜플: ', t)
print('튜플 정렬된 리스트: ', sorted(t))
print()
s = 0
for i in lst:
    s += i
print('합:', str(s) + ', 항목수:', len(lst))
print('최대:', str(max(lst)) + ', 최소:', str(min(lst)) + ', 평균:', s / 10)