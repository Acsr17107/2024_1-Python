import pickle as pk

with open('worldcup.bin', mode = 'rb') as fromf, open('2018worldcup.bin', mode = 'wb') as tof:
    while True:
        one = fromf.read(1)
        if not one:break
        tof.write(one)

with open('2018worldcup.bin', mode = 'rb') as tof:
    a = pk.load(tof)
    b = pk.load(tof)
    
print(a)
print(b)