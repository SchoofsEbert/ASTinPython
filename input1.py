def func(x):
    return x + 4


class Foo(object):
    def __init__(self):
        self.x = 2

    def bar(self):
        self.x += 1


func(10)
f = Foo()
f.bar()
