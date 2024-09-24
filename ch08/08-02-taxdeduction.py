# 종합 소득 과세 표준 구간에 다른 기준 총합 소득
base = (0, 12_000000, 46_000000, 88_000000, 150_000000, 300_000000, 500_000000)
# 종합 소득 과세 표준 구간에 따른 세율
rate = [6, 15, 24, 35, 38, 40, 42]

# 세율 15%에 대한 누진 공제액
brate = rate[1]; 
deduction1  = (base[1] - base[0]) * (brate - rate[0])/100

# 세율 24%에 대한 누진 공제액
brate = rate[2]; 
deduction2  = (base[1] - base[0]) * (brate - rate[0])/100 # 1천 2백만 원의 누진 공제
deduction2 += (base[2] - base[1]) * (brate - rate[1])/100 # 3천 6백만 원의 누진 공제

# 세율 35%에 대한 누진 공제액
brate = rate[3]; 
deduction3  = (base[1] - base[0]) * (brate - rate[0])/100 # 1천 2백만 원의 누진 공제
deduction3 += (base[2] - base[1]) * (brate - rate[1])/100 # 3천 6백만 원의 누진 공제
deduction3 += (base[3] - base[2]) * (brate - rate[2])/100 # 4천 2백만 원의 누진 공제

# 세율 38%에 대한 누진 공제액
brate = rate[4]; 
deduction4  = (base[1] - base[0]) * (brate - rate[0])/100 # 1천 2백만 원의 누진 공제
deduction4 += (base[2] - base[1]) * (brate - rate[1])/100 # 3천 6백만 원의 누진 공제
deduction4 += (base[3] - base[2]) * (brate - rate[2])/100 # 4천 2백만 원의 누진 공제
deduction4 += (base[4] - base[3]) * (brate - rate[3])/100 # 6천 2백만 원의 누진 공제

# 세율 40%에 대한 누진 공제액
brate = rate[5]; 
deduction5  = (base[1] - base[0]) * (brate - rate[0])/100
deduction5 += (base[2] - base[1]) * (brate - rate[1])/100
deduction5 += (base[3] - base[2]) * (brate - rate[2])/100
deduction5 += (base[4] - base[3]) * (brate - rate[3])/100
deduction5 += (base[5] - base[4]) * (brate - rate[4])/100

# 세율 42%에 대한 누진 공제액
brate = rate[6]; 
deduction6  = (base[1] - base[0]) * (brate - rate[0])/100
deduction6 += (base[2] - base[1]) * (brate - rate[1])/100
deduction6 += (base[3] - base[2]) * (brate - rate[2])/100
deduction6 += (base[4] - base[3]) * (brate - rate[3])/100
deduction6 += (base[5] - base[4]) * (brate - rate[4])/100
deduction6 += (base[6] - base[5]) * (brate - rate[5])/100

# 계산된 누진 공제액 출력
print('누진 공제 1: {:10,.0f}원'.format(deduction1))
print('누진 공제 2: {:10,.0f}원'.format(deduction2))
print('누진 공제 3: {:10,.0f}원'.format(deduction3))
print('누진 공제 4: {:10,.0f}원'.format(deduction4))
print('누진 공제 5: {:10,.0f}원'.format(deduction5))
print('누진 공제 6: {:10,.0f}원'.format(deduction6))