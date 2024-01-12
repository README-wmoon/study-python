# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다
menu_message = "메뉴선택 "
chooose_num = "1. 빨간색\n2. 검은색\n3. 노란색\n4. 흰색"

print(chooose_num)
menu = int(input(menu_message))
result = ''

if(menu == 1):
    result = f"Red"

elif(menu == 2):
    result = f"black"
elif(menu == 3):
    result = f"yellow"
else:
    result = f"white"

print(result)