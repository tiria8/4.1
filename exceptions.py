class BaseError(Exception):
    message = 'Неизветная ошибка'

class RequestError(BaseError):
    message = 'Ошибка обработки запроса'

class CourierError(BaseError):
    message = 'Ошибка доставки'

class NotEnoughSpace(CourierError):
    message = 'Недостаточно места на складе'

class NotEnoughProduct(CourierError):
    message = 'Недостаточно товара на складе'

class TooManyDifferentItems(CourierError):
    message = 'Слишком много разных товаров'

class InvalidRequest(RequestError):
    message = 'Неверный запрос'

class InvalidStoreName(RequestError):
    message = 'Неверный склад'