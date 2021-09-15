from abc import ABC, abstractmethod


class Observer(ABC):
    @staticmethod
    @abstractmethod
    def send(message=''):
        pass


class EmailNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"1 - Sending email message {message}")
        

class SMSNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"2 - Sending sms message {message}")


class PushNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"3 - Sending push message {message}")

