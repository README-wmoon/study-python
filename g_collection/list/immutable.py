import copy

# 얕은 복사 -> list안에 어떤 요소를 변경시켠 새로운 list로 변환시켜준다.
#               -> 대신 list안에 다른 자료들이 있을경우 두번 이상 접근해야한다. -> mutable
# 얕은 복사는 기존 값을 복사해서 새롭게 만들어내는 것을 의미한다.
# 새로운 주소에 할당하기 때문에, 불변성이 보장된다.
datas = [1, 2, 3]
datas_copy = copy.copy(datas) # 주소가 다르다 -> False
# datas_copy = datas # 이거는 주소가 같다 -> True
# print(datas is datas_copy)
datas_copy[0] = 10
print(datas)
print(datas_copy)


# 얕은 복사
datas = [1, 2, 3]
datas_copy = datas[:] # 얕은 복사를 지원한다 -> 주소값은 다르다 -> 근데 왜 이걸 쓸까 -> 하지만 8번쨰 줄을 더 많이 선호한다.
datas_copy[0] = 10
print(datas)
print(datas_copy)

# 얕은 복사
# 얕은 복사 사용 시, 두 번째 접근부터는 불변성이 보장되지 않는다.
datas = [1, [1, 2, 3], [4, 5, 6]]
datas_copy = copy.copy(datas) # 얕은 복사라 한층만 복사한다
datas_copy[0] = 10
print(datas)
print(datas_copy)

datas_copy[1][0] = 10 # 한층만 복사가 되기 떄문에 두층을 같이 사용하면 주소값이 같아서 같은 값이 나오게 된다.
print(datas)
print(datas_copy)

# 깊은 복사 사용 시, 깊은 접근까지 모두 불변성이 보장된다
# 너무 깊은 구조에서 사용할 때에는, 메모리 소모량이 증가하기 떄문에,
# 불변성이 보장될 필요가 없을 때에는 사용하지 않는 것이 좋다.

# 깊은 복사
datas = [1, [1, 2, 3], [4, 5, 6]]
datas_copy = copy.deepcopy(datas)
datas_copy[1][0] = 10
print(datas)
print(datas_copy)