uyear = {1:'freshman', 2:'sophomore', 3:'junior', 4:'senior'}

try:
    y = int(input('대학교 몇 학년이지요? '))
    if y > 4 or y < 1:
        raise Exception('1~4 정수를 입력하세요.')

except Exception as e:
    print('예외 발생 이름:', type(e))
    print('예외 발생 이유:', e)

else:
    print('{}학년: {}'.format(y, uyear[y]))

finally:
    print('예외 처리가 잘되는군요!')