# 인덱스 슬라이싱
animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start=0 : exlusive_end=len(list)] -> list
print(animals[0])
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])

# list[inclusive_start=0 : exlusive_end=len(list) : step=1] -> list -> step은 많이 안쓰임 -> 메모리때문에
food = ['noodle', 'meat', 'bread', 'chicken']
print(food[:3:2])
print(food[2::2])

# 역순 출력
print(food[::-1])

number_list = list(range(1, 11))

#실습
# # [1, 3, 5, 7, 9]
# print(number_list[:9:2])
# # [6, 5, 4, 3, 2]
# print(number_list[5:0:-1])
# # [2, 4, 6]
# print(number_list[1:6:2])
# # [2, 3, 4, 5, 6, 7]
# print(number_list[1:7])


animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

# 기존 값은 사라지고 zoo list 안에 있는 요소가 각각 들어간다.
animals[1:2] = zoo
print(animals)

# 기존 값은 뒤로 밀리고 해당 자리에 값이 들어간다.
animals.insert(animals.index('dog') + 1, 'giraffe')
print(animals)

# 기존 값은 뒤로 밀리고 zoo list 통채로 들어간다.
animals.insert(animals.index('dog') + 1, zoo)
print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog', 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']
zoo1 = ['hamster', 'fish']
zoo2 = ['dog', 'whale']
animals[1:2] = zoo1
animals[3:4] = zoo2

print(animals)