def print_info():

    def function_info(func):

        def argument_info(*args):
            computed = func(*args)
            string = '{}: {} -> {}'.format(func.__name__, args, computed)
            print(string)
            return computed
        return argument_info
    return function_info


@print_info()
def get100():
    return 100


@print_info()
def func1(x, y):
    return get100() + x + y + 1


func1(4, 6)
