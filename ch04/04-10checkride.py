maxnum = 4
maxheight = 130

more = True
cnt = 0
while more:
    height = float(input("키는 ? "))
    if height < maxheight:
        cnt += 1
        print('입장하세요. 현재 %d명' % cnt)
    else:
        print('키 제한 입장불가.')
    if cnt == maxnum:
        more = False
else:
    print('%d명 모두 찼습니다. 다음 번에 이용하세요.' % cnt)