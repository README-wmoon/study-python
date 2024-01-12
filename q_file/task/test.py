# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

datas = './alice.txt'
count = 0
words_count = {}
with open(datas, 'r', encoding='utf-8') as file:
    for line in file.read():
        line = file.read()
        # print(line)
        # words = file.read()
        # words = words.lower()
        # words.split(" ")
        # # print(words)
        # if words not in words_count:
        #     words_count[words] = 1
        # else:
        #     words_count[words] += 1

        # for line in file.read():
        #
        #     if len(line) < 2:
        #         line = line.lower()
        #         print(line)

        # words = line.split()
        # print(words)
        # for word in words:
        #     if len(word) < 2:
        #         word = word.lower()
        #         # print(word)
        #         if word not in words_count:
        #             words_count[word] = 1
        #         else:
        #             words_count[word] += 1

for key, value in words_count.items():
    print(f'{key}, {value}')

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""