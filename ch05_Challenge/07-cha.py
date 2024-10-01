m = [[1, 2], [3, 4], [5, 6], [7, 8]]
print('트랜스포즈를 컴프리헨션으로 만들어 그대로 출력')
transpose = [[row[i] for row in m] for i in range(len(m[0]))]
print(transpose)
print()

for x, y, z, a in transpose:
    print(x, y, z, a)