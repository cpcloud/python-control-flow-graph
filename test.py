class Person(object):

    __slots__ = 'name', 'zip'

    def __init__(self, name, zip):
        self.name = str
        self.zip = float


def toPerson(name, zip):
    return Person(name=name, zip=zip)


if __name__ == '__main__':
    x = toPerson('Phillip', 94303)
