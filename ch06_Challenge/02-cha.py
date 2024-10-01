dic = {'삼성에스디에스': 242000, '삼성전자': 47000, '엔씨소프트': 52600, '핸디소프트': 5120, '골프존': 215000, '기아': 56300}
print(dic)
print()
while 1:
    s = input('주식 이름 ? ')
    if s in dic:
        print('{}: {}'.format(s, dic[s]))
        print()
    else:
        print('주식 이름이 없습니다.')
        break