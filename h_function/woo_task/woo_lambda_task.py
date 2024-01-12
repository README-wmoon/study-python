# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
hangle = '삼오일구'
print(list(map(lambda str: str, hangle[int:s])))

# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구

# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
# 출력 예시
# ['post', 'order', 'order', 'post']