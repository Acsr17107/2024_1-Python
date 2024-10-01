m = [[1, 2], [3, 4], [5, 6], [7, 8]]
print('원 행렬(m) 출력: ')
for i in m:
    for j in i:
        print(j, end=' ')
    print()
print()
print('전차 행렬 출력:')
for i, j in m:
    print(i, end = ' ')
print()
for i, j in m:
    print(j, end = ' ')