class A:

    @classmethod
    def __new__(cls, *args, **kwargs): # A()가 생략되어있다. -> 생성자 -> 메모리에 필드에 할당하는 애 -> 얘가 진짜 생성자임
        print('__new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, data1, data2, name=''): # 이것도 생성자 하지만 다름 -> 여러분이 원하는 걸 받아서 처리한다. -> 이것을 많이 쓰긴하는데 진짜는 아님
        print('__init__')
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    def print_name(self):
        print(self.name)

a = A(10, 20, 'a')
print(a) # __init__의 self와 주소값이 같음
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2) # 값이 나옴 -> 동적바인딩 떄문에
# a.print_name('a')
a.print_name()

b = A(100, 200, 'b')
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()