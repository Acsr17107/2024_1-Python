for i in range(3):
    coffee = input("주문 [아메리카노] [에스프레소] [카라멜 마끼아또] >> ")

    if coffee == '아메리카노':
        print('%s 주문' % coffee)
    elif coffee == '에스프레소':
        print('%s 주문' % coffee)
    elif coffee == '카라멜 마끼아또':
        print('%s 주문' % coffee)
    else:
        print('주문 오류')
else:
    print('주문 마침')