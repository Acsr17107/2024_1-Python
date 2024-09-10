from math import factorial as fact
from statistics import median, mean, variance, stdev

for i in range(1, 17, 5):
    print('{}! = {}'.format(i, fact(i)))
print()

st = [80, 99, 77, 65, 92, 74, 82]
print(st)
print('중앙 값: {:.2f}'.format(median(st)))
print('평균: {:.2f}'.format(mean(st)))
print('분산: {:.2f}'.format(variance(st)))

if __name__ == '__main__':
    print('표준편차: {:.2f}'.format(stdev(st)))