# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# email_id, domain = input("이메일 입력 ").split('@')
# fomatting = f"나의 이메일 아이디는 {email_id} 도메인은 {domain}"
# print(fomatting)

# email_id, domain = input("Enter your email id: ").split("@")
# formatting = f'나의 이메일 아이디는 {email_id} 도메인은 {domain}'
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# time1, time2 = input("몇시 몇분: ").split(':')
# print(f'현재 시간은 {time1}시 {time2}분 입니다')

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
# firstNum, middleNum, endNum = input('번호를 입력하시오: ').split('-')
# print(f'핸드폰 번호는 {firstNum}이고 {middleNum}이고 {endNum}')

# 이름과 나이를 한 번에 입력받은 뒤 "OOO님의 나이는 OOO살" 형식으로 출력
# name, age = input('이름 나이 입력\nex)문우람,28\n').split(',')
# print(f'{name}님의 나이는 {age}살')

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
number1, number2, number3 = map(int, input('숫자를 입력하시오: \nex)1+3+4\n').split('+'))
print(number1+number2+number3)
