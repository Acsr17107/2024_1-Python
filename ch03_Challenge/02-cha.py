s = input('다섯 문자 이상의 문자열 입력 >> ')
print('입력 문자열:', s)
print('첫 문자:', s[0])
print('마지막 문자:', s[-1])
print('첫 문자를 제외한 부분 문자열:', s[1:])
print('마지막 문자를 제외한 부분 문자열:', s[:-1])
print('맨 앞과 뒤의 두 문자씩을 제외한 부분 문자열:', s[2:-2])
print('문자 하나씩을 건너뛴 부분 문자열:', s[::2])
print('역문자열', s[::-1])