# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.

# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

# class Taxi:
#     normal_fare = 5800
#     normal_distance = 2
#     texi_per_km = 1000
#
#     def __init__(self, money, distance):
#         self.money = money
#         self.distance = distance
#
#     def calculate_distance(self):
#         cost = Taxi.normal_fare
#         if self.distance > Taxi.normal_distance:
#             cost += (self.distance - Taxi.normal_distance) * Taxi.texi_per_km
#
#         return cost
#
#     def get_money(self):
#         return self.money - self.calculate_distance()
#
#
# taxi = Taxi(20000, 1)
# print(taxi.calculate_distance(), taxi.get_money())


# 2. 택시 객체 생성 시 택시 수익을 초기화한다.
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)

# class Taxi:
#     def __init__(self, money=0):
#         self.money = money
#
#     def fare_distance(self):
