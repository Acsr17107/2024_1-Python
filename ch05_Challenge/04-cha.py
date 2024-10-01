data = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
rsum = []
csum = []
a = 0
b = 0

for i in range(3):
    a = sum(data[i])
    rsum.append(a)

for i in range(3):
    for j in range(3):
        b += data[j][i]
    csum.append(b)
    b = 0

print('각 행의 합:', rsum)
print('각 열의 합:', csum)