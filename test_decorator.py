from datetime import datetime


def log_time(func):

    def wrapped_function(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(end - start)

        return int(result) * 2

    return wrapped_function


@log_time
def test1(): 
    return input('enter sth ... ')


def test2(): pass


if __name__ == '__main__':
    x = test1()
    print(x)
    test2()