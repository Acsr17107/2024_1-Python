LCD = [[ "|||||", 
         "|   |", 
         "|   |", 
         "|   |", 
         "|||||" ], 
         
        ["   | ", 
         "  || ", 
         "   | ", 
         "   | ", 
         " ||||" ], 
         
        ["|||||", 
         "    |", 
         "|||||", 
         "|    ", 
         "|||||" ], 
         
        ["|||||", 
         "    |", 
         "|||||", 
         "    |", 
         "|||||" ], 
         
        ["|   |", 
         "|   |", 
         "|||||", 
         "    |", 
         "    |" ], 
         
        ["|||||", 
         "|    ", 
         "|||||", 
         "    |", 
         "|||||" ]]

ROW = 5 # 디지털 숫자의 높이

def printLCD(digit):
    """
    '234'의 문자열 숫자를 디지털 숫자로 출력하는 함수
    
    인자
        digit: 출력하려는 정수 형태의 문자열
    """

    # 한 행에 출력하려는 여러 자릿수 각 행을 출력
    for row in range(ROW):
        # 출력하려는 자릿수만큼 디지털 행을 출력
        for i in range(len(digit)):
            # '32'라면 각각 3에 대해 row행, 2에 대해 row행 순으로
            num = int(digit[i])
            # 각 행을 한 줄에 계속 출력
            print(LCD[num][row], end = ' ')
        # 다음 줄로 이동
        print()

# 문자열의 문자가 '012345'가 아니면 False 반환
def checkdgt(s):
    tag = True
    for c in s:
        if c not in '012345':
            tag = False
            break
    return tag
# 표준 입력
snum = '7'
while not checkdgt(snum):
    snum = input("0 ~ 5 자릿수로만 정수 형태(예 523, 24501) 1개 입력 >> ")
# 출력
printLCD(snum)