class Singleton:

    
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


if __name__ == '__main__':
    s1 = Singleton('Mohammad')
    s2 = Singleton('Amin')
    s3 = Singleton('Ali')
    s4 = Singleton('Farahnaz')

    print(id(s1))
    print(id(s2))
    print(id(s3))

    print(id(s1) == id(s2) == id(s3))
