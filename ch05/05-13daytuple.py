day1 = ('monkey', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday')
# ('sunday')로 하면 튜플이 아니고 문자열
day3 = ('sunday', )

day = day1 + day2 + day3
print(type(day))
print(day)

day = day1 + day2 + day3 * 3
print(day)