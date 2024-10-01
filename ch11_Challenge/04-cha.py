f = open('cp.txt', 'w')
f.write('freshman\n')
f.write('sophomore\n')
f.write('junior\n')
f.write('senior\n')
f.close()

with open('cp.txt', 'r') as file:
    for line in enumerate(file, start=1):
        print('{}학년 {}'.format(*line), end='')