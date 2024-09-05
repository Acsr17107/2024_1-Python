c = int(input('온도 입력 >> '))
fahrenhite = c * 9/5 + 32
f = c * 2 + 30
dif = fahrenhite - f
print('정확 계산: 섭씨:', c , ',', '화씨:', fahrenhite)
print('약식 계산: 섭씨:', c , ',', '화씨:', f)
print('차이:', dif)