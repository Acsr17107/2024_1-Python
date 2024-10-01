try:
    print(int(oct(10)))

except ValueError as e:
    print('예외 발생 이름:', type(e))
    print('예외 발생 이유:', e)

else:
    print('잘 실행됐습니다.')

finally:
    print('예외 처리가 잘되는군요!')
    print()

try:
    print(int(oct(10)[2:]))

except ValueError as e:
    print('예외 발생 이름:', type(e))
    print('예외 발생 이유:', e)

else:
    print('잘 실행됐습니다.')

finally:
    print('예외 처리가 잘되는군요!')