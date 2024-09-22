str = input('2개의 단어를 빈 공간으로 구분해 입력하세요. >> ')
pos = str.find(' ')
preword = str[:pos]
postword = str[pos+1:]
print(preword, postword)
print(preword[::1], postword[::-1])