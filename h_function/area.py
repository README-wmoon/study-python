# 전역 변수(global variable)
# 지역 밖에 선언된 변수
# 여러 함수에서 공유해야 하는 값이 있을 겨우 사

# 지역 변수(local variable)
# 어떤 지역 안에 선언된 변수

# 전역 변수
count = 0


def increase():
    # print(count)
    # 지역 변수
    # count = 0
    # 위에서 global이라고 쓰이면 아래쪽은 다 전역변수로 쓰인다.
    global count # 전역변수를 수정하려면 global 키워드를 사용한다
    count += 1

increase()
print(count)