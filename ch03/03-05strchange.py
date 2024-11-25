str = input('2개의 단어 사이 공백 입력 >> ')
pos = str.find(' ')
preWord = str[:pos]
postWord = str[pos+1:]
print(preWord, postWord)
print(preWord[::-1], postWord[::-1])