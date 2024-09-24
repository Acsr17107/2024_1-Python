# 종합 소득 과세 표준 구간에 따른 기준 종합 소득
base = (0, 12_000000, 46_000000, 88_000000, 150_000000, 300_000000, 500_000000)
# 종합 소득 과세 표준 구간에 따른 세율
rate = [6, 15, 24, 35, 38, 40, 42]

# 누진 공제 금액 계산
deduction = [] # 빈 누진 공제 금액
for i in range(len(base)-1):
    dmoney = 0
    brate = rate[i+1]
    # 구간에서의 누진 공제액을 계산해 합
    for j in range(i+1):
        dmoney += (base[j+1] - base[j]) * (brate - rate[j])/100
    deduction.append(dmoney) # 누진 공제 리스트에 추가

taxtable = []
for i, r in enumerate(rate):
    section = []
    # 종합 소득 과세 표준 문자열 생성해 추가
    if i == 0:
        s = '{}원 초과 ~ {:,.0f}만 원 이하'.format(0, base[i+1]/10_000)
    elif i == 6:
        s = '{:,.0f}억 원 초과 ~ {}'.format(base[i]/100_000000, '계속')
    else:
        s = '{:,.0f}만 원 초과 ~ {:,.0f}만 원 이하'.format(base[i]/10_000, base[i+1]/10_000)
    section.append(s)

    # 소득세율 문자열 생성해 추가
    s = '{}%'.format(rate[i])
    section.append(s)
    # 누진 공제액 문자열생성해 추가
    if i == 0:
        s = '-'
    else:
        s = '{:,.0f}만 원'.format(deduction[i-1]/10_000)
    section.append(s)
    # 구간의 행 추가
    taxtable.append(section)

print(' 종합 소득 과세 표준 표 '.center(48, '*'))
for i, row in enumerate(taxtable):
    print(' {:^}. {:^28} {:^4} {:^10}'.format(i+1, row[0], row[1], row[2]))