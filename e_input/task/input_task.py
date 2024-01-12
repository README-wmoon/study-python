# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# email_id, domain = input("이메일 입력 ").split('@')
# fomatting = f"나의 이메일 아이디는 {email_id} 도메인은 {domain}"
# print(fomatting)

'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
    round(값, 원하는 자리수_: 소수점이 맞춰진 결과값
'''
yard = 91.44
inch = 2.54
yard_input = float(input("야드를 입력하시오 "))
inch_input = float(input("인치를 입력하시오 "))

yard_total = yard * yard_input
inch_total = inch * inch_input

fomatting2 = f"{yard_input} yard는 {round(yard_total, 2)}cm\n{inch_input} inch는 {round(inch_total,2)}cm"
print(fomatting2)