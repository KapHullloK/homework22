from classes.request import Request
from classes.shop import Shop
from classes.store import Store


def main():
    shop = Shop(items={
        "коробки": 1,
        "чипсы": 5,
        "огурцы": 10
    })
    store = Store(items={
        "печеньки": 5,
        "бананы": 5,
        "груши": 5
    })

    print("Приветствую! Здесь вы можете заказать товар!")
    user = '\033[1m' + '\nUser:' + '\033[0m'
    print("Сейчас хранится:\n"
          "В складе хранится:")
    store.get_info()
    print("В магазине хранится:")
    shop.get_info()
    print("Заказ должен выглядеть так:\nДоставить 3 печеньки из склад в магазин")

    while True:
        request, count = get_request(user)[0], get_request(user)[1]

        if request.order[0].lower() == "доставить":
            try:
                store.remove(request.product, count)
            except Exception:
                continue

            try:
                shop.add(request.product, count)
            except Exception:
                continue
            break

    print("В складе хранится:")
    store.get_info()

    print("В магазине хранится:")
    shop.get_info()


def get_request(user):
    while True:
        try:
            request = Request(input(user))
            cr = check_request(request)
            if request.is_valid() and cr:
                return [request, cr]
            print("Вы ввели запрос не так как в примере!")
            continue

        except IndexError:
            print("Вы ввели запрос не так как в примере!")


def check_request(request):
    try:
        count = int(request.amount)
    except ValueError:
        print("Вы не ввели количество продукта, попробуйте снова")
        return False

    if request.from_place.lower() != "склад":
        print("Вы не ввели откуда доставить товар, попробуйте снова")
        return False

    if request.to_place.lower() != "магазин":
        print("Вы не ввели куда доставить товар, попробуйте снова")
        return False

    return count
