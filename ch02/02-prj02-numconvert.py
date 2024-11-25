# 진수, 정수 입력
base = int(input('입력할 정수의 진수 >> '))
invar = input(str(base) + '진수 정수 입력 >> ')
data = int(invar, base) # invar을 base진수로 변환

print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))