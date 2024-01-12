# try:
#     number = int(input('정수를 입력하세요.'))
#
# except ValueError as e:
#     print('정수만 입력해주세요~!')
#
# print('반드시 실행되어야 하는 문장')

# try:
#     print(10 / 0)
#
# except ZeroDivisionError as e:
#     print(e) # __str__로 재정의했다 -> 따라서 주소값이 아니고 String 값이 나온다.
#     print('0으로 나누어서는 안됩니다.')

# except Exception: # Exception은 모든 에러의 부모이다.

# datas = [1, 2, 3]
#
# try:
#     print(datas[3])
#     # 위의 문장에서 오류가 발생하지 않는다면 실행한다.
#     print('오류가 없어요!')
#
# except ValueError:
#     pass
#
# except IndexError:
#     print('인덱스를 확인해주세요!')
#
# else:
#     # try에 작성한 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요!')
#
# finally:
#     print('반드시 실행되어야 하는 문장')

# nickname = input('닉네임: ') # 실행은 되는데 나중에 문제가 있을때
# if nickname == '멍청이':
#     raise RuntimeError # raise를 써서 일부러 오류를 발생시킨다.

class BardWordError(Exception):
    def __str__(self):
        return "비속어는 사용할 수 없습니다."

def check_bad_word(message):
    if '멍청이' in message:
        raise BardWordError

chat = input('채팅: ')
try:
    check_bad_word(chat)
    print(chat)

except BardWordError as e:
    print(e)