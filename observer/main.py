from shop import Product, Purchase
from notification import EmailNotification

if __name__ == '__main__':
    p1 = Product()
    p2 = Product()
    p3 = Product()
    p4 = Product()

    # order the first purchase
    purchase = Purchase([p1, p2, p3, p4])
    purchase.checkout()
    purchase.cancel()
