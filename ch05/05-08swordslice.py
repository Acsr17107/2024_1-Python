wlist = ['밥', '삶', '길', '죽', '꿈', '차', '떡', '벅', '말']
print('wlist[:] = ', wlist[:])
print('wlist[::] = ', wlist[::])
print('wlist[::-1] = ', wlist[::-1])
# 오름차순
print(wlist[::3])
print(wlist[1::3])
print(wlist[2::3])
# 내림차순
print(wlist[::-2])
print(wlist[-1:-8:-3])
# 오름과 내림차순의 혼재
print(wlist[1:-1:])
print(wlist[-2:-9:-3])