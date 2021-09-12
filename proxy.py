COUNTRIES = ['Iran', 'Germany']
VAT = {"Iran": 0.09, "Germany": 0.35}


def checkout_permission(func):
    def wrapped_function(obj, user): # obj = self 
        if obj.user == user:
            return func(obj)
        return 'you are not allowed to checkout !!'
    return wrapped_function


class User:
    pass


class Address:
    def __init__(self, country):
        self.country = country


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.products_list = []

    def add_products(self, product_list):
        if not isinstance(product_list, list):
            product_list = [product_list]
        self.products_list.extend(product_list)

    def total_price(self):
        s = 0
        for product in self.products_list:
            s += product.price
        return s

    @checkout_permission
    def checkout(self):
        print(f"checkout done!")


def calculate_vat(func):
    def wrapper_func(pur):
        vat = VAT[pur.address.country]
        total_price = pur.total_price()
        return total_price + total_price * vat
    return wrapper_func


def show_total_price(p):
    return p.total_price()


@calculate_vat
def show_vat_plus_price(p):
    return p.total_price()


if __name__ == '__main__':
    user = User()
    addr_iran = Address(country=COUNTRIES[0])
    addr_germany = Address(country=COUNTRIES[1])

    p1 = Product('Laptop Asus', 600)
    p2 = Product('S21 Samsung', 1100)
    p3 = Product('Tabriz Rug', 300)

    products = [p1, p2, p3]

    purchase = Purchase(user=user, address=addr_iran)

    purchase.add_products(products)
    print(
        f"pure price: {show_total_price(purchase)}\tprice with tax: {show_vat_plus_price(purchase)}")
    user2 = User()
    print(purchase.checkout(user))
    print(purchase.checkout(user2))