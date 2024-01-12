# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.


# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]



# 쿠폰 할인율을 주문금액에 순차 적용하는 함수를 만들기
# 함수에(*args, **kwargs) 값을 넣어준다
# unpacking으로 쓰였다.
# def coupon_disscount(*args, **kwargs):
#     # 주문 금액을 리스트 형태로 바꿔서 쓰인다
#     pay = list(args)
#     # 쿠폰 할인율을 1 - 쿠폰 * 0.01로 계산한다.
#     coupon_rate = 1 - kwargs.get('coupon') * 0.01
#     # 카운트를 받아온다.
#     count = kwargs.get('count')
#     # 주문금액 안에서 아이템-갯수가 0보다 크거나 같으면 아이템에 넣어준다
#     # 그렇지 않으면 아이템 * 할인율을 반올림 해주어서 넣어준다
#     result = [item if args.index(item)-count >= 0 else round(item * coupon_rate) for item in args]
#     # c_price = pay * int((100 - coupon_rate))
#     # result로 반환한다.
#     return result
#
# # 쿠폰의 디스카운트 메소드 안에서 금액 값을 넣고 쿠폰이랑 갯수를 출력해준다.
# print(coupon_disscount(1000,4000,5000, coupon=30, count=100))

# packing으로 쓰였을 떄
def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''

    if 'coupon' in kwargs:
        return [
            # 그 방에 있는 주문 금액
            int((1- kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None

print(use_coupon(1000, 2000, 3000, coupon=50, count=2))

# if result:
#     print(result)
# else:
#     print('쿠폰이 없습니다')