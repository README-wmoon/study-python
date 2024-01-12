# animals = ["dog", "cat", "bird", "fish"]
# print(animals)
# print(type(animals))
#
# # 인덱스로 접근
# print(animals[1])
# print(animals[2])
#
# # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
# print(animals[-1])
# print(animals[-2])
#
# # len()
# print(len(animals))
#
# # append()
# animals.append("hamster")
# print(len(animals))
# print(animals)
#
# animals.append("cat")
# print(animals)
#
# # insert()
# animals.insert(1, "dog")
# print(animals)
#
# # remove()
# animals.remove('fish')
# print(animals)
#
# # del()
# # del(animals[1]) # 밑에꺼랑 같다 둘다 똑같음
# del animals[1]
# print(animals)
#
# # clear()
# # animals.clear()
# # print(animals)
#
# # index()
# print(animals.index('bird'))
# # print(animals.index('tiger'))
#
# # 수정
# index = animals.index('bird')
# animals[index] = 'lion'
# print(animals)
#
# # 그 외
# animals = ["dog", "cat", "bird", "fish"]
# print(animals * 2)
#
# print("dog" in animals)
# print("tiger" in animals)
#
# for animal in animals:
#     print(animal)

# 실습
# 1~90까지 list에 담고 출력
# for number in range(90):
#     numbers = [number + 1]
#     print(numbers)
# print(type(numbers))

# list에 1~90 까지 담기
# number_list = [0] * 90
#
# for문 안에 length로 하여 리스트 담기
# for i in range(len(number_list)):

# 리스트안에 i+1을 넣기
#     number_list[i] = i + 1

# 1~100까지 중 짝수만 list에 담고 출력
numbers = [0] * 100


for i in range(len(numbers)):
    numbers[i] = i + 1
    # print(type(numbers)) # list
    if numbers[i] % 2 == 0:
        print(type(numbers[i])) # int
# print(type(numbers))

# 강사님
# number_list = []
#
# for i in range(len(number_list)):
#     number_list[i] = (i + 1) * 2
#     print(number_list)

# # 1~10까지 list에 담은 후 짝수만 출력
# for number in range(10 % 2):
#     print(number)

# number_list에 선언
# number_list = []
#
# for i in range(10):
#     number_list.append(i + 1)
# print(number_list)
#
# for i in range(len(number_list)):
#     print(type(number_list))
#     if number_list[i] % 2 == 0:
#         print(number_list[i])
# even_list = []
# for i in range(len(number_list)):
#     if number_list[i] % 2 == 0:
#         even_list.append(number_list[i])
# print(even_list)

# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# 회원추가
# users = ['철수', '영수', '민수', '똘이']
# print(users)
#
# # 영수 라는 회원의 번호를 선언
# index = users.index('영수')
#
# # 영희 선언
# users[index] = "영희"
# print(users)
#
# # 3번쨰 인덱스 삭제
# del users[3]
# print(users)

# list안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
# print(number_list[0][0])
length = len(number_list) * len(number_list[0])

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])