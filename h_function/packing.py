# unpacking: 값을 풀어서 적는 것
# def get_total(number1, number2, number3):
#     return number1 + number2 + number3
import string


# packing: 값을 묶어서 적는 것
def get_total(*numbers):
    # 외부에서 전달받은 값들이 numbers(튜플)에 저장된다
    print(type(numbers))
    total = 0
    for number in numbers:
        total += number
    return total

# 여러 개의 값을 콤마로 구분하여 전달한다
# total = get_total(1, 2, 3, 4, 5)
# print(total)

# 여러 개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통쨰로 들어가게 된다.
# 즉, 결과는 다음과 같다. ([1, 2, 3, 4, 5],)
# 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다
# numbers = [1, 2, 3, 4, 5]
# total = get_total(*numbers)
# print(total)

# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# def total_score(*scores):
#
#     total = 0
#
#     for score in scores:
#         total += score
#
#     return total
# # packing으로 제작하기
# total = total_score(30, 40, 50)
# print(total)
#  def get_count_of_result(target, keyword):
#     # return len([i for i in target if i == keyword])
#     count = 0
#     for i in target:
#         if i == keyword:
#             count += 1
#     return count
# 문자열에서 'A'가 몇개 있는지 검사하는 함수
def get_count_of_A(*strs):
    # return [str.count("A") for str in strs]
    count = 0
    counts = []
    for str in strs:
        for s in str:
            if s == "A":
                count += 1
        counts.append(count)
        count = 0
    return counts

print(get_count_of_A("AAA", "AAC"))