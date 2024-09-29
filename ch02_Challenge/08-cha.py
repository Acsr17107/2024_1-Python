num1 = int(input('네 자릿수 정수 입력 >> '))
unit1 = 1000
unit2 = 100
unit3 = 10
t, num2 = divmod(num1, unit1)
h, num3 = divmod(num2, unit2)
ten, one = divmod(num3, unit3)
one = one * unit1
ten = ten * unit2
h = h * unit3
print(one + ten + h + t)