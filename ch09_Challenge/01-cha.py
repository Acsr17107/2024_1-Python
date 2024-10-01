from math import pi
from random import random

def getarea(r):
    s = pi * r * r
    return s

n = random() * 10
r = round(n, 2)
print('원의 반지름: {}'.format(r))
print('원주율 pi: {:0.4f}'.format(pi))
print('반지름 {}인 원의 면적은 {:.2f}'.format(r, getarea(r)))