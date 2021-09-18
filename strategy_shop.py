class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


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

    def checkout(self):
        self.payment.pay()


class Getway:
    def __init__(self, name):
        self.name = name


class Payment:
    getways = (Getway("G1"), Getway("G2"))

    def __init__(self, purchase):
        self.purchase = purchase

    def get_getway(self):
        return self.getways[0] if self.purchase.total_price() < 200 else self.getways[1]

    def pay(self):
        getway = self.get_getway()
        print(f"Payment is being paid through: {getway.name}")


if __name__ == '__main__':
    p1 = Product('p1', 100)
    p2 = Product('p2', 200)
    p3 = Product('p3', 300)

    purchase = Purchase()

    purchase.add(p1)
    print(purchase.total_price())
    purchase.checkout()
    purchase.add([p2, p3])
    print(purchase.total_price())
    purchase.checkout()

    print(purchase.__dict__)