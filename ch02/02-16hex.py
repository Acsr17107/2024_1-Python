invar = input('16진수 정수 입력 >> ')
data = int(invar, 16) # 16진수로 인지

print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))