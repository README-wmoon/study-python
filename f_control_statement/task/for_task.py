# 1~15까지 출력
# for number in range(1, 16):
#     print(number)
# 30~1까지 출력
# for number in range(30, 0, -1):
#     print(number)
# 1~100가지 중 홀수만 출력
# for number in range(1, 100, 2):
#     print(number)
# 1~10까지 합 출력
# sum = 0
# for number in range(1, 11, 1):
#     sum = sum + number
# print(sum)
# 1~n까지 합 출력
# n = int(input("숫자입력: "))
# for number in range(1, n, 1):
#     sum = sum + number
# print(sum)
# 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(3, 6 ,1):
#     for j in range(3, 7):
#         print(j, end=' ')

# '1,235,500'를 1235500으로 출력
# number = '1,235,500'
# for number in number:
# result = ''
# for i in number:
#     if i != ',':
#         result = result + int(i)
# print(number)