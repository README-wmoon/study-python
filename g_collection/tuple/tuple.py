# mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10

#data_list2를 바꿧는데 data_list1도 같이 바뀐다.
print(data_list2)
print(data_list1) # 이렇게는 쓰지말자

# immutable: 변할 수 없는
# 튜플은 값을 한번쓰면 수정할 수가 없다
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# data_tuple2[0] = 10
#데이터가 값을 튜플을 수정하려면 list를 통해서 해야된다.
test = list(data_tuple2)
test[0] = 10
print(test)

#값은 바꿀수 없되, 뒤에 연결은 할 수 있다.
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
print(data_tuple1)

# 튜플을 사용하는 방식
# 튜플은 사용은 하되, 수정은 하지말라
datas = 1, 2
print(type(datas))

# 에러코드 즉 회사에서 다른 개발자가 바꾸지말라고 쓸떄, 개발자들이 봐서 이것을 변경할 수 없다고 알아야된다.
# 파이썬은 상수가 없기 떄문에 지금같이 튜플형태로 쓰여야된다 ex) final ERROR_CODE = 1; -> 자바
ERROR_CODE = 1,
print(type(ERROR_CODE[0]))
