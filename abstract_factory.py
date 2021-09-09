from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass


class RugsDetail(DetailBase):
    pass


class Rugs(ProductBase):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def detail(self):
        return RugsDetail()

    @property
    def price(self):
        return PriceDetail()


class GiftCard:

    def __init__(self, company, min_price, max_price):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price

    @property
    def detail(self):
        return GiftCardDetail()

    @property
    def price(self):
        return GiftCardPrice()


if __name__ == '__main__':
    r1 = Rugs('Esfehan', 150)
    r2 = Rugs('Mashhad', 200)

    g1 = GiftCard('Google', 20, 60)
    g2 = GiftCard('Apple', 30, 50)

    products = [r1, r2, g1, g2]

    for product in products:
        pass
