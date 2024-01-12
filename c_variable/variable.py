# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30

print(a, b, c, sep=', ')

a, b, c = 100, 200, 300
print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33

print(a, b)

# temp = a
# a = b
# b = temp
# print(a, b)

a, b = b, a
print(a, b)

# 동적 바인딩
a = 10
print(type(a))

a = 10.5
print(type(a))

a = 'A'
print(type(a))

a = "ABC"
print(type(a))

a = ['A', 'B', 'C']
print(type(a))

a = {'A': 1, 'B': 2, 'C': 3}
print(type(a))

a = True
print(type(a))

# 변수명 주의사항
a = {10, 10.5, 'A', "ABC"}
print(type(a))

data = 10
print(type(data))

score = 10.5
print(type(score))

grade = 'A'
print(type(grade))

people = "ABC"
print(type(people))

# 서식문자
# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우에 버림을 하여 짝수로 만들어준다
# 예를 들어 53.45는 43.4로, 32.75는 32.8로 반올림한다
# 이를 오사오입(round-to-nearest-even)이라고 한다
name = '한동석'
age = 20
height = 157.45

print("오사오입~~~!!!!")
print("이름: %s" % name)
print("나이: %d" % age)
print("키: %.1f" % height)
print("키: %.1f" % (round(height + 0.0000000000001, 1)))
# print("이름: %s\n나이: %d살\n키: %.1fcm" % (name, age, height))
# print('%04d' % 1)


# format 함수
name = '홍길동'
age = 80
height = 156.26

print('이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height))
print('이름: {0}\n나이: {2}\n키: {1:.1f}'.format(name, age, height))
print('이름: {name}\n나이: {age}\n키: {height:.1f}'.format(name=name, age=age, height=height))

formatting1 = '이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height)
formatting2 = '이름: {0}\n나이: {2}\n키: {1:.1f}'.format(name, age, height)
formatting3 = '이름: {name}\n나이: {age}\n키: {height:.1f}'.format(name=name, age=age, height=height)
print(formatting1)
print(formatting2)
print(formatting3)


print("=" * 20)
formatting = '이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height)
print(formatting)


# format string
name = '한동석'
age = 20

# round(실수값 반올림 자리수)
print(f'이름: {name}')
print(f'나이: {age}살')
print(f'키: {round(height, 1)}')

# print(f'이름 : {name}')

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래형식으로 출력하기
# 1 + 3 = 4
num1 = 1
num2 = 3
print(f'{num1} + {num2} = {num1 + num2}')

# 실습2(format 함수)
# 아래 메세지를 format함수를 사용하여 출력한다
# Hello 파이썬, Python is fantastic
# Hello 장고, Django is fantastic
# Hello 리액트, React is fantastic

p = "Python"
p_name = "파이썬"
d = "Django"
d_name = "장고"
r = "React"
r_name = "리액트"

formatting1 = 'Hello {}, {} is fantastic'.format(p_name, p)
formatting2 = 'Hello {}, {} is fantastic'.format(d_name, d)
formatting3 = 'Hello {}, {} is fantastic'.format(r_name, r)
print(formatting1)
print(formatting2)
print(formatting3)

# 실습2 fString
# 아래 메세지를 format함수를 사용하여 출력한다
# Hello 파이썬, Python is fantastic
# Hello 장고, Django is fantastic
# Hello 리액트, React is fantastic
print("=" * 20)
print(f'Hello {p_name}, {p} is fantastic')
print(f'Hello {d_name}, {d} is fantastic')
print(f'Hello {r_name}, {r} is fantastic')