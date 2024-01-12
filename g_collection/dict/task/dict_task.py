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

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 새로운 이름, 가격 추가
        new_name, new_price = input(append_message).split()
        # 새로운 이름이 딕셔너리안에 있지 않으면 들어가기
        if new_name not in data_dict:
            # 딕셔너리 안에 새로운 이름이 가격에 추가가 됨
            data_dict[new_name] = int(new_price)
            continue

        # 만약 아닐시, 오류 메세지가 뜬다.
        else:
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 수정할 이름 입력
        name = input(search_name_message_for_update)
        # 만약 딕셔너리 안에 이름이 있으면 들어가기
        if name in data_dict:
            # 수정이 입력될 이름이 이름과, 가격에 넣어진다
            new_name, new_price = input(update_message).split()
            # 만약 딕셔너리 안에 이름이 없으면
            if new_name not in data_dict:
                # 이름이 딕셔너리 데이터 안에 삭제된다.
                del data_dict[name]

                # 이름과 가격이 대입이 된다.
                data_dict[new_name] = int(new_price)
                continue
            # 만약 딕셔너리 안에 이름이 있으면
            else:
                # 이름과 가격이 대입이 된다.
                data_dict[new_name] = int(new_price)
        #딕셔너리 안에 이름이 없으면
        else:
            # 에러 메세지가 나온다.
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 이름을 입력하였을때
        name = input(delete_message)
        # 만약 이름이 딕셔너리 안에 있을 때
        if name in data_dict:
            # 딕셔너리 안에 이름이 지워진다.
            del data_dict[name]
            continue

        # 만약 이름이 딕셔너리 안에 없으면
        else:
            # 에러 메세지가 뜬다.
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 상품명 검색
            keyword = input(search_name_message)
            # 만약 상품명이 딕셔너리 안에 있을때
            if keyword in data_dict:
                # 가격, 이름을 딕셔너리 안을 반복
                for name, price in data_dict.items():
                    # 만약 상품명이랑 딕셔너리 안에 이름이랑 같으면
                    if keyword == name:
                        # 출력 검사
                        print(f'{name}, {price}')
                continue

            # 만약 아닐시
            else:
                # 에러메시지 출력
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # flag 만듬
            check = False
            # 가격 검색명
            price_input = int(input(search_price_message))
            # 50% ~ 150% 안에 오차범위 계산
            min = price_input * 0.5
            max = price_input * 1.5

            # 딕셔너리 안에 이름이랑 가격을 넣어준다
            # 만약 가격이 max 보다 작거나 같고 min 보다 크거나 같으면
            for name, price in data_dict.items():
                if min <= price <= max:
                    # flag를 True로 만들어준다
                    check = True
                    print(f'{name}, {price}')
            # 만약 flag면
            if check:
                # continue를 쓰인다.
                continue

            # 만약 flag가 아니면
            if not check:
                # 에러 메세지가 뜬다.
                result_message = search_error_message

    # 목록
    # 5번쨰로 들어간다.
    elif choice == 5:
        # 만약 딕셔너리 길이가 0이랑 같으면
        if len(data_dict) == 0:
            # no_item_message가 출력된다.
            result_message = no_item_message
        else:
            # 딕셔너리 안에 이름이랑 가격을 넣어주면
            for name, price in data_dict.items():
                # 이름, 가격 출력해준다
                print(f'{name}, {price}')
                # continue를 써준다
                continue

    # 나가기
    elif choice == 6:
        # break를 써주어서 while 문을 나간다.
        break

    # 그 외
    else:
        result_message = error_message

    # continue가 없거나 수행이 다끝났을 경우에는
    # result_message를 출력한다.
    print(result_message)
    result_message = ""






