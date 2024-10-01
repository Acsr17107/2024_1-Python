def divide(x, y):
    z = x / y
    return z

try:
    divide(3.2, 2)

except ZeroDivisionError as e:
    print('0으로는 나눌 수 없습니다.')

else:
    print('결과:', divide(3.2, 2))

try:
    divide(5.4, 0)

except ZeroDivisionError as e:
    print('0으로는 나눌 수 없습니다.')

else:
    print('결과:', divide(5.4, 0))