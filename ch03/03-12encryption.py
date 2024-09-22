orgPwd = int(input('ID로 사용할 여덟자리의 정수를 입력하세요 >> '))
keyMask = 27182818 # 키로 사용할 정수 하나를 저장
encPwd = orgPwd ^ keyMask # ID를 암호화하여 저장
print('입력한 ID: %d' % orgPwd)
print('암호화해 저장된 ID: %d' % encPwd)
inPwd = int(input('로그인할 ID를 입력하세요 >> '))
result = encPwd ^ keyMask # 키로 암호화된 것을 복호화
print('로그인 성공: {}'.format(inPwd == result))