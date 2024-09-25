f = open('pyzen.txt', 'r')

while True:
    line = f.readline()
    if not line: break
    print(line, end = '')
    # print(line.strip('\n'))

f.close()