user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]
#
#
# # 추가(초보자용)
def insert(*, number, name):
    '''

    :param number: 회원 번호
    :param name: 회원 이름
    '''
    user_info.append({'number': number, 'name': name})

# # 추가
# # 회원 번호는 자동 증가한다.
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
#
# # 목록
# def select_all():
#     return user_info
#
#
# # 조회(번호로 조회)
def select(number):
    for user in user_info:
        if user['number'] == number:
            return user
    return {}

#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
# print(delete(1))
# print(user_info)

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# post_info 안에 number 자동완성 하려고 만들었음
# 전역변수
count = 5
# 조회수 증가 시키려고 만듬
# 전역변수
read_count = 0

# user_insert 라는 함수를 만들어 title, content,file, read_count 라는 매개변수를 만들었음
# def user_insert(*, title, content, file, read_count):
#     갯수를 쓰려고 만듬
#     global count

#     갯수 증가
#     count += 1
#     post_info에 append를 써서 title, content, file, read_count를 추가시켰다.
#     post_info.append({'number': count, 'title': title, 'content': content, 'file': file, 'read_count': 0})
#
# # print(user_insert(title='바보니', content='진짜 바보넴', file='/usr/post/file/img006.png'))


# # 목록(최신순으로 조회)
# user_select라는 이름으로 함수를 만듬
# def user_select():
#     post_info(최신순)-> slicing을 써서 반환 시켰다
#     return post_info[::-1]
#
# print(user_select())


# 조회(번호로 조회, 조회수 1 증가)
# user_info라는 함수 안에 number라는 매개변수를 만듬
def user_info(number):
    # 전역 변수 read_count를 선언함
    global read_count
    # read_count를 1 증가시킴
    read_count += 1
    # post_info 안에 user을 받아 반복문을 썻음
    for user in post_info:
        # 만약 user의 'number'라는 것이 매개변수 number랑 일치한다면
        if user['number'] == number:
            # user의 'read_count'안의 read_count라는 값을 대입시켜라 -> +1
            user['read_count'] = read_count
            # user을 반환시킨다
            return user
    # None을 반환시킨다.
    return None
# print(user_info(1))

# 수정(번호로 정보 수정)
# 업데이트라는 함수에 keyword argument 라는 매개변수 만듬
# def update(**kwargs):
#     kwargs.get('content')에서 수정한 것을 user_select의 이름안의 content 안에 수정시킴
#     user_select(kwargs.get('number'))['content'] = kwargs.get('content')

# def user_update(post)

# print(update())

# 삭제(번호로 삭제)

# user_delete라는 함수에 매개변수 숫자를 넣음
# def user_delete(number):

#     post_info의 user_info(number)의 인덱스 값을 지워버림
#     del post_info[post_info.index(user_info(number))]
#
# print(user_delete(3))
# print(post_info)