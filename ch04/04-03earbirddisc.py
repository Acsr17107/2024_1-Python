from time import localtime

hour = localtime().tm_hour
min = localtime().tm_min

if hour < 10:
    print('현재 시각: %d시 %d분, 조조 할인 가능. ' % (hour, min))
else:
    print('현재 시각: %d시 %d분, 조조 할인 불가능. ' % (hour, min))