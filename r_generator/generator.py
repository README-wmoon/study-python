import os
import psutil

# process_object = psutil.Process(os.getpid())
# memory_before = process_object.memory_info().rss / 1024 / 1024
#
# data_list = [i**2 for i in range(10000)]
# print(data_list)
#
# memory_after = process_object.memory_info().rss / 1024 / 1024
# print(f'memoery : {memory_before} -> {memory_after}')
#
# #############################
# process_object = psutil.Process(os.getpid())
# memory_before = process_object.memory_info().rss / 1024 / 1024
#
#
# data_generator = (i ** 2 for i in range(100))
# print(next(data_generator))
#
# memory_after = process_object.memory_info().rss / 1024 / 1024
# print(f'memoery : {memory_before} -> {memory_after}')

def increase(number: int = 0):
    while True:
        number += 1
        yield number # return의 기능을 가지고있지만 다른점은 next로 받아야 된다 -> generator 객체를 쓴다.

result = increase()
while True:
    data = input("Y/n >> ")
    if data == "Y":
        print(next(result))

    else:
        break