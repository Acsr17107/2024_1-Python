h, w = input('당신의 키(cm)와 몸무게(kg)는? >> ').split()
H = float(h)
W = float(w)
b = W / (H / 100)**2
print('키:', str(H) + '(cm), 몸무게:', str(W) + '(kg)')
if 40 <= b:
    print('BMI: {:.1f} 고도 비만'.format(b))
elif 35 <= b < 40:
    print('BMI: {:.1f} 중등도 비만'.format(b))
elif 30 <= b < 35:
    print('BMI: {:.1f} 비만'.format(b))
elif 25 <= b < 30:
    print('BMI: {:.1f} 과체중'.format(b))
elif 18.5 <= b < 25:
    print('BMI: {:.1f} 정상'.format(b))
elif b < 18.5:
    print('BMI: {:.1f} 저체중'.format(b))