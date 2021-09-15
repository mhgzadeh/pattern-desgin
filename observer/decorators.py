def notify_observers(message=''):
    def decorated_method(func):
        def wrapped(self):  # self = obj
            result = func(self)
            for observer in self.observers:
                observer.send(message)
            return result

        return wrapped

    return decorated_method
