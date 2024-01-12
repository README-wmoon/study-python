# 중복이 없고, 순서가 없다
# 중복제거 할떄 씀
# 값이 있는지 없는지 검사하려고 한다.
# 예) MBTI, 혈액형
# 중괄호에 컴마가 하나씩 연결되어 있으면 set이다
world_set = {'korea', 'america', 'japan', 'china'}
print(type(world_set))
print(len(world_set))

# set은 값의 순서가 없어서 가져오지 못하니 리스트로 형변환 해서 하자
# print(world_set[1])
world_set.add('korea')
# set은 값을 다른 자료구조를 통해 가져와서 출력해줘서 지금 보시는것은 set이 아니다.
print(world_set)

# 중복을 제거할 때 효과적이다.
datas = [1, 1, 3, 2, 3, 4, 1, 4, 4]
print(list(set(datas)))