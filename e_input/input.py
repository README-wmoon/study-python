# 문자열끼리만 연결(+)이 가능하다!
# data = 3
# print('안' + str(data))

# name = input("이름: ")
# formatting = f'{name}님 환영합니다'
# print(formatting)

# 제 이름은 ???, 키는 ??cm입니다
# centimeter = input("키: ")
# formatting1 = f"제 이름은 {name}, 키는 {centimeter}cm 입니다."
# formatting2 = "제 이름은 {names}, 키는 {cm} 입니다.".format(names = name, cm =centimeter)
# print(formatting1)
# print(formatting2)

# 두 정수를 입력받은 후 곱셈 결과 출력
# num1 = int(input("첫번째 숫자 입력 "))
# num2 = int(input("두번째 숫자 입력 "))
# sum = num1 + num2
# formatting3 = f"{num1} + {num2} = {sum} 이다"
# print(formatting3)

# map쓰는 이유 -> 랜더링 효율 -> 여러개를 한번에 동일하게 바꿔주는 함수
# map(어떻게 바꿀 것인가, [])
# number1, number2 = map(int, input('두 정수를 입력하세요\nex)1, 3\n').split(','))
# print(number1 + number2)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
time1, time2 = map(int, input("시간입력: ").split(':'))
formatting = f"현재 {time1}시 {time2}입니다."
print(formatting)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
cellphoneNum1, cellphoneNum2, cellphoneNum3 = map(str, input("핸드폰 번호 입력 ").split("-"))
formatting2 = f"핸드폰 앞자리 번호는 {cellphoneNum1} 중간자리 번호는 {cellphoneNum2} 뒤자리 번호는 {cellphoneNum3}"
print(formatting2)

# 이름과 나이를 한 번에 입력받은 뒤 "OOO님의 나이는 OOO살" 형식으로 출력
name,age = map(str, input("이름 나이 입력 \nex)문우람 30\n").split(' '))
formatting3 = f"{name}님의 나이는 {age}살 입니다"
print(formatting3)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
num1, num2, num3 = map(int, input("정수 입력 \nex)10,20,30\n").split(','))
sum = num1 + num2 + num3
formatting4 = f"{num1} + {num2} + {num3} = {sum}\n"
print(formatting4)