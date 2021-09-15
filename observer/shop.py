from decorators import notify_observers
from notification import EmailNotification, SMSNotification, PushNotification


class Product:
    pass


class Payment:
    observers = [EmailNotification, PushNotification]
    
    @notify_observers(message='Purchase paid.')
    def checkout(self):
        pass

class Purchase:
    observers = [EmailNotification, SMSNotification, PushNotification]
    
    def __init__(self, product_list):
        self.product = product_list
        self.payment = Payment()
        # self.is_paid = False

    def checkout(self):
        self.payment.checkout()
        # self.is_paid = True
        # print('print self: ', self.observers, self.is_paid)
    
    @notify_observers(message='Purchased canceled.')    
    def cancel(self):
        pass
