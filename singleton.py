class CommonClass:
    ...

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


c1 = CommonClass()
c2 = CommonClass()

s1 = Singleton()
s2 = Singleton()

print('CommonClass c1: ', c1)
print('CommonClass c2: ', c2)

print('CommonClass s1: ', s1)
print('CommonClass s2: ', s2)
