class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print('create')
        else:
            print('recycle')
        return cls.instance
        return cls.instance