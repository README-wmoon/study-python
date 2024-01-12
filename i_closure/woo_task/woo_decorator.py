# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.

def average(original_function):
    def operate(*args, **kwargs):
        count = len(args)
        total = 1
        if count != 0:
            for i in args:
                total *= i

            print(f'args총합: {total}')
        else:
            total = kwargs['total'] / kwargs['count']
            print(f'kwags총합 {total}')
        return original_function(*args, **kwargs)
    return operate



@average
def set_datas(*args, **kwargs):
    count = len(args)
    total = 0
    if count != 0:
        for number in args:
            total += number
        print(f'args총합 {total}')

    else:
        total = kwargs.get('total') / kwargs.get('count')
        print(f'kwargs: {total}')



set_datas(1, 2, 3, 4, 5)
set_datas(total=100, count=5)