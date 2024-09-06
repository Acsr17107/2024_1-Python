time = input('시각 정보(16:30:15) 입력 >> ')
print('입력 시간 정보:', time)
hours, mins, secs = time.split(':')
print(hours + '시 ' + mins + '분 ' + secs + '초')