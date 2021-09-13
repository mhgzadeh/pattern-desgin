from time import sleep


class LazyLoader:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object == None:
            self.object = self.cls()
        return getattr(self.object, item)


class MySQLHandler:
    def __init__(self):
        sleep(3)

    def get(self, name):
        return f'Hello from MySQL. {name}'


class MongoHandler:
    def __init__(self):
        sleep(4)

    def get(self):
        return 'Hello from Mongo'


class NotificationCenterHandler:
    def __init__(self):
        sleep(2)

    def get(self):
        return 'Hello from Notif'


if __name__ == '__main__':
    mysql = LazyLoader(MySQLHandler)
    mongo = LazyLoader(MongoHandler)
    notif = LazyLoader(NotificationCenterHandler)

    print(mysql.get('Mohammad'))
    print(notif.get())
    
    print(mysql.get('Amin'))
    print(notif.get())
    
    print(mysql.get('Ali'))
    print(notif.get())
    
    print(mysql.get('Farahnaz'))
    print(notif.get())