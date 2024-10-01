import pickle as pk

wc = {2010: '남아프리카공화국', 2014: '브라질'}
win = ['스페인', '독일']

with open('worldcup.bin', mode = 'wb') as f:
    pk.dump(wc, f)
    pk.dump(win, f)

with open('worldcup.bin', mode = 'wb') as f:
    wc[2018] = '러시아'
    win.insert(2, '프랑스')
    pk.dump(wc, f)
    pk.dump(win, f)

with open('worldcup.bin', mode = 'rb') as f:
    a = pk.load(f)
    b = pk.load(f)

print(a)
print(b)