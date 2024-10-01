korean = ('정렬', '초보자', '내포', '사전')
english = ('sorting', 'novice', 'comprehension', 'dictionary')
while 1:
    w = input('찾을 단어 입력 ? ')
    if w in korean:
        print(english[korean.index(w)])
    else:
        print('다시 입력해주세요.')