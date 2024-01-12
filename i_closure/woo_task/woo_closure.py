# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.
def set_product(*args):
    count = 0

    for i in args:
        count += 1
        i['count'] = count

    def product_insert(**kwargs):
        nonlocal count, args
        count += 1
        args += {'count': count, 'name': kwargs['name'], 'price': kwargs['price']},

    def product_update(**kwargs):
        for product in args:
            if product['count'] == kwargs['count']:
                product['price'] = kwargs['price']
                product['name'] = kwargs['name']

    def product_select_all():
        return args

    return {'product_insert': product_insert, 'product_update': product_update, 'product_select_all': product_select_all}

products = [
    {'name': '발화성', 'price': 50000, 'count': 1},
    {'name': '유리', 'price': 30000, 'count': 2}
]

product_service = set_product(*products)
print(product_service.get('product_select_all')())
print(product_service.get('product_update')(name='철수', price=20000, count=2))
print(product_service.get('product_select_all')())
print(product_service.get('product_insert')(name='훈이', price=70000))
print(product_service.get('product_select_all')())
