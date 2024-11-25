digit = input('실수(세 자리.두 자리) 입력 >> ')
num = digit.replace('.', '')

sum = 0
sum += int(num[0])
sum += int(num[1])
sum += int(num[2])
sum += int(num[3])
sum += int(num[4])

print('입력값:', digit)
print('모든 자릿수 합:', sum)