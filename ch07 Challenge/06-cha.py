from random import sample

lst = sorted(sample(range(1, 31), 6))
flst = list(filter(lambda x: x%3 == 0, lst))

print('원 리스트:', lst)
print('필터 리스트:', flst)