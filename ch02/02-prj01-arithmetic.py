num1 = float(input('첫 번째 수 입력 >> '))
num2 = float(input('두 번째 수 입력 >> '))
print('합:', num1 + num2)
print('차:', num1 - num2)
print('곱:', num1 * num2)
print('나누기:', num1 / num2)

expression = input('연산식 입력(예 2.1 + 3 * 3.2) >> ')
print('연산식:', expression, '결과:', eval(expression))