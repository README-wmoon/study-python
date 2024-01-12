boolean = False
while not boolean:
    value = input("4조장 이름은? ")
    condition1 = value == '박유진'
    condition2 = value == '박지원' or value == '문우람' or value == '백시현' or value == '김규일'
    if condition1:
        print('정답입니다.')
        boolean = True
    elif condition2:
        print('팀원 이름입니다. 조장이름을 입력하세요')
    else:
        print('다시입력하세요')