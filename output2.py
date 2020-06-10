def wrapper(func, *args):
    computed = func(*args)
    string = '{}: {} -> {}'.format(func.__name__, args, computed)
    print(string)
    return computed


def get100():
    return 100


def func1(x, y):
    return wrapper(get100) + x + y + 1


wrapper(func1, 4, 6)
