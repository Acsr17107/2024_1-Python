category = int(input('원하는 음료는? 1. 커피 2. 주스 '))

if category == 1:
    menu = int(input('번호 선택 1. 아메리카노 2. 에스프레소 3. 카라멜 마끼아또 '))
    if menu == 1:
        print('1. 아메리카노 선택')
    elif menu == 2:
        print('2. 에스프레소 선택')
    elif menu == 3:
        print('3. 카라멜 마끼아또 선택')
else:

    menu = int(input('번호 선택 1. 망고주스 2. 수박주스 3. 자몽주스 '))
    if menu == 1:
        print('1. 망고주스')
    elif menu == 2:
        print('2. 수박주스')
    elif menu == 3:
        print('3. 자몽주스')