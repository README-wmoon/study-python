# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."


def insert(**kwargs):
    '''

    :param kwargs: {'name': '상품명', 'price': 가격}
    '''
    # 이름에 상품명 그리고 가격의 가격 value를 이름이랑, 가격에 넣어주었다.
    name, price = kwargs.values()
    # 딕셔너리 이름안에 가격이랑 같이 써주었다.
    data_dict[name] = int(price)


def update(*, name, new_name, new_price):
    del data_dict[name]
    data_dict[new_name] = int(new_price)


def delete(name):
    del data_dict[name]

def select_by_name(keyword):
    result = {}
    if keyword in data_dict:
        result = {'name': keyword, 'price': data_dict[keyword]}

    return result

def select_by_price(price, range=50):
    result = []
    min = price * range * 0.01
    max = price * (range * 0.01 + 1)

    for name, price in data_dict.items():
        if min <= price <= max:
            result.append({'name': name, 'price': price})

    return result

def select_all():
    return data_dict

# while 문 접속
while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        new_name, new_price = input(append_message).split()

        # 만약 select_by_name안에있는 함수에 사람 이름이 없으면
        if len(select_by_name(new_name)) == 0:
            # insert 함수에 새로운 이름이랑 가격을 선언하였다.
            insert(name=new_name, price=new_price)
            continue
        else:
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 수정할 상품명 입력
        name = input(search_name_message_for_update)

        # 상품명 안에 이름이 없으면
        if len(select_by_name(name)) != 0:
            # 사용자가 입력하고, 새로운 이름이랑, 새로운가격을 넣어준다
            new_name, new_price = input(update_message).split()
            # 만약 이름이 있을때
            if len(select_by_name(new_name)) == 0:
                # update 함수를 적용 시킨다.
                update(name, new_name, new_price)
                continue
            # 만약 이름이 없으면
            else:
                # 이름과 가격을 대입시킨다.
                data_dict[new_name] = int(new_price)
        # 상품명안에 이름이 없을 때
        else:
            # 에러 메세지를 적용시킨다.
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 삭제할 이름을 입력했을때
        name = input(delete_message)
        # 만약 삭제할 이름이 있을 때
        if len(select_by_name(name)) != 0:
            # delete(name) 함수를 적용시킨다.
            delete(name)
            continue
        # 만약 삭제할 이름이 없으면
        else:
            # 에러 메세지를 적용시킨다.
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 검색 이름을 입력하였을 때
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 검색할 이름을 입력하였을 때
            keyword = input(search_name_message)
            # select_by_name 함수를 result에 대입한다.
            result = select_by_name(keyword)
            # 만약 result 안에 상품명이 있으면
            if len(result) != 0:
                # 이름이랑 가격을 출력시켜준다.
                print(f"{result.get('name')}, {result.get('price')}")
                continue

            # 만약 result 안에 상품명이 없으면
            else:
                # 에러 메세지를 적용시킨다.
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 가격을 입력하였을 때
            price_input = int(input(search_price_message))

            # select_by_price 함수를 result에 적용시킨다.
            result = select_by_price(price_input)

            # 만약 가격 이름이 있을떄
            if len(result) != 0:

                # result 안에 있는 것을 반복 돌렸을떄
                for product in result:
                    # 이름이랑 가격을 출력시켜준다
                    print(f"{product.get('name')}, {product.get('price')}")
                continue

            # 가격 이름이 없으면
            else:
                # 에러 메세지를 적용시킨다.
                result_message = search_error_message

    # 목록
    elif choice == 5:
        # 만약 상품명이 아무것도 없을때
        if len(select_all()) == 0:
            # 에러 메세지를 적용시킨다.
            result_message = no_item_message
        # 만약 상품명이 있으면
        else:
            # 딕셔너리 안에 이름이랑, 가격을 반복문을 돌렸을떄
            for name, price in data_dict.items():
                # 이름이랑 가격을 출력시켜준다.
                print(f'{name}, {price}')
                continue

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        result_message = error_message

    # 마지막 나가면서 에러메시를 적용하며 나간다.
    print(result_message)
    result_message = ""






