from random import randint
lst = []
for i in range(10):
    a = randint(1, 99)
    lst.append(a)
print('리스트', lst)
print('정렬 리스트', sorted(lst))
print('역순 리스트', sorted(lst, reverse=1))