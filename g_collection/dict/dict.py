# student = {
#     "name": "한동석",
#     "email": "tedhan1204@gmail.com"
# }
#
# print(student['name'])
# print(student.get('name'))
#
# # get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# # default 값이 없을 때에는 None을 가져온다.
# # print(student['phone']) # 오류
# print(student.get('phone', '01012341234'))
#
# # 'name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다.
# student['name'] = '홍길동'
# print(student)
#
# # 'phone' key 값이 없기 때문에, 아래의 코드는 '추가'이다.
# student['phone'] = '01012341234'
# print(student)
#
# if 'email' in student: # 수정
#     student['email'] = 'hgd1234@gmail.com'
# else: # 추가
#     student['email'] = 'hgd1234@gmail.com'
#
# print(student)

# my_dict = {
#     1: "한동석",
#     "two": "20살",
#     False: [10, 20, 30],
#     "row": [
#         {"name": "ted", "age": 40},
#         {"name": "jack", "age": 30},
#         {"name": "john", "age": 20}
#     ]
# }

# row에 있는 회원 3명의 정보를 모두 출력
# my_dict 안에 모든 것 출력
# for i in my_dict:
#     print(my_dict[i])

# 강사님
# if 'row' in my_dict:
#     print(my_dict['row'])
#     for data in my_dict['row']:
#         print(f'{data["name"]}, {data["age"]}')

# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하며, 홀수만 출력한다.
# dict를 사용한다

# even_number = 2, 4, 6, 8, 10
# odd_number = 1, 3, 5, 7, 9
# number_dict = {
#     "짝수" : even_number,
#     "홀수" : odd_number
# }
#
# input_number = input("홀수 짝수 입력하시오: ")
# if input_number in number_dict:
#     print(number_dict[input_number])

# 강사님
# number_dict = {
#     '홀수' : [i * 2 + 1 for i in range(5)],
#     '짝수' : [(i + 1) * 2 for i in range(5)]
# }
# print(", ".join(number_dict[input('짝수 혹은 홀수 ')]))
# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수 ')])))

# number_dict = {
#     True : [i * 2 + 1 for i in range(5)],
#     False : [(i + 1) * 2 for i in range(5)]
# }

# print(", ".join(number_dict[input('짝수 혹은 홀수 ')]))
# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수 ') == '홀수'])))

student = {
    "name": "한동석",
    "email": "tedhan1204@gmail.com"
}

# key 분리
# list로 분리해서 써야된다.
print(list(student.keys()))

# value 분리
# 요것도 list로 분리해서 써야됨
print(list(student.values()))

# item 분리
print(list(student.items()))

for key, value in student.items():
    print(key, value)



