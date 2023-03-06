from courier import Courier
from exceptions import CourierError, RequestError
from request import Request
from shop import Shop
from store import Store

store = Store(items={})
shop = Shop(items={})

storages = {
    "магазин": shop,
    "склад": store
}

store.items = {
    "печенька": 20,
    "пончик": 25,
    "коробки": 3,
    "собачки": 10,
    "цветы": 15
}

shop.items = {
    "печенька": 1,
    "пончик": 2,
    "коробки": 1,
    "собачки": 2,
    "цветы": 3
}

def main():
    print('Добрый день!')

    while True:
        for i in storages:
            print(f'В {i} хранится:\n {storages[i].items}')

        user_input = input(
            'Введите запрос по типу "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", чтобы закончить программу\n'
        )

        if user_input in ['stop', 'стоп']:
            break

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as e:
            print(e.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except CourierError as e:
            print(e.message)

if __name__ == '__main__':
    main()
