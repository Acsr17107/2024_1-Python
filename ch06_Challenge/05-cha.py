fruits = ['apple', 'banana', 'grapes', 'pear']
prices = (1000, 500, 1200, 1500)
dic = dict(zip(fruits, prices))
print(dic); print()

for i, j in enumerate(dic, start=1):
    print('{} {} 가격: {}'.format(i, j, prices[i - 1]))