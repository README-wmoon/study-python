# number = 15
#
# if number % 3 == 0:
#     print(f"{number}는 3의 배수입니다")
#
# if number % 5 == 0:
#     print(f"{number}는 5의 배수입니다")

# number 가 양수인지, 음수인지, 0인지 검사
# number1, number2 = map(int, input("숫자를 입력하시오\nex)1,3\n").split(","))
# number = number1 / number2
#
# positive_condition = number >= 0
# negative_condition = number < 0
#
# if(positive_condition):
#     print("음수입니다")
# elif(negative_condition):
#     print("양수입니다")
# else:
#     print("0입니다")

# 나이를 입력받은 후 미성년자인지 검사
# age = int(input("나이입력 "))
# condition = 0 < age < 18
# error_condition = age <= 0
#
# if condition:
#     print('미성년자입니다')
# elif error_condition:
#     print("잘못 입력 하셨습니다")
#
# else:
#     print("성인 입니다")

# 두 정수를 입력받은 후 대소비교 진행
number1, number2 = map(int,input('두 정수를 입력 하시오 \nex(10/2)\n').split("/"))
first_winner = number1 > number2
second_winner = number1 < number2
#선언할 떄 넣을 값을 모를 경우 초기값을 넣어준다
# 정수: 0
# 실수: 0.0
# 문자열: '' 또는 ""
# 불린: false
result_message = ''

# 개별처리
if(first_winner):
    print("number1이 이겼습니다")
elif(second_winner):
    print("number2가 이겼습니다")
else:
    print("무승부 입니다")

# 일괄처리란,
# 각 분기별로 결과를 처리하지 않고,
# 모든 분기 종료 후 한번에 처리하는 것을 의미한다
if(first_winner):
    result_message = f'큰값 : {number1}'
elif(second_winner):
    result_message = f'큰값 : {number2}'
else:
    result_message = f'같은값'

print(result_message)

# 문제
