class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Payment:
    def __init__(self, purchase):
        self.purchase = purchase


class Purchase:
    def __init__(self):
        self.products = list()
        self.payment = Payment(self)

    def add(self, product):
        if isinstance(product, list):
            self.products.extend(product)
        else:
            self.products.append(product)

    def total_price(self):
        return sum([p.price for p in self.products])


if __name__ == '__main__':
    p1 = Product('p1', 100)
    p2 = Product('p2', 200)
    p3 = Product('p3', 300)

    purchase = Purchase()

    purchase.add(p1)
    print(purchase.total_price())
    purchase.add([p2, p3])
    print(purchase.total_price())
