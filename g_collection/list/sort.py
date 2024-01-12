# 정렬
number_list = [5, 4, 6, 1, 3]

# 1. sort() - 하지만 문제점이 있다 -> 원본이 그대로 변경이 되서 다른 개발자에게 불편해짐
# number_list.sort(reverse=True)
# print(number_list)

# 2. sorted() - 원본은 유지되고 새로운 list가 만들어짐
sorted_list = sorted(number_list, reverse=True)
print(number_list)
print(sorted_list)

