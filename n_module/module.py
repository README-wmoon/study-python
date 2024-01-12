import calc_add
# import calc.calc_sub
import calc.calc_sub as sub
from calc.calc_sub import sub
# from calc.calc import Calculator
from calc.calc import *

import os
import sys

print(sys.path) # 등록이 되어있는 경로
print(os.path.abspath(os.path.dirname(__file__))) # 내가 현재 작업하는 경로
# print(sys.path.append(os.path.abspath(os.path.dirname(__file__)))) # 실행시키면 내가 현재 작업하는 경로가 추가가된다.

# if __name__ == '__main__':
#     print(calc_add.add(2, 3))
#     # print(calc.calc_sub.sub(10, 5))
#     # print(sub.sub(10, 5))
#     print(sub(10,5))
#     print('=' * 20)
#     c = Calculator(10, 5)
#     print(c.add())
#     print(c.sub())