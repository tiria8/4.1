from courier import Courier
from exceptions import CourierError, RequestError
from request import Request
from shop import Shop
from store import Store

store = Store(items={
    "печенька": 20,
    "пончик": 25,
    "коробки": 3,
    "собачки": 10
})
shop = Shop(items={
    "печенька": 3,
    "пончик": 5,
    "коробки": 1,
    "собачки": 2
})
storages = {
    "магазин": shop,
    "склад": store
}

def main():
    print('Добрый день!')

    while True:
        for i in storages:
            print(f'В {i} хранится:\n {storages[i].get_items()}')

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

        courier = Courier(request=Request, storages=storages)

        try:
            courier.move()
        except CourierError as e:
            print(e.message)

if __name__ == '__main__':
    main()