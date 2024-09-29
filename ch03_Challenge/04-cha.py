url = 'https://docs.python.org/3/tutorial'
a = url.replace(':', '')
b = a.replace('/', '')
print(b[0:b.find('d')])
print(b[b.find('d'):b.find('3')])
print(b[b.find('3') + 1:])