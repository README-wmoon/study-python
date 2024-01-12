# 1~15까지 출력
print(list(filter(lambda i: i, [i + 1 for i in range(15)])))
for i in range(15):
    print(i + 1, end='')

# 30~1까지 출력
print(list(filter(lambda i: i < 31, [i+1 for i in range(30)])))
for i in range(30):
    print(30 - i)
