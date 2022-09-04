def decorator(fun):
    def wrapper():
        print("Witaj")
        return fun()
    return wrapper

@decorator
def fun():
    print("funkcja 1")

fun()

class decorator_class(object):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("Dekorator")
        return self.fun(*args, **kwargs)

@decorator_class
def fun2(name):
    print(name + " wita funkcja 2")

fun2("Ziomek")

def decorator_with_arguments(arg):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            print("Witaj " + arg)
            return fun(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_arguments("Tomek")
def fun3(name):
    print("Wita funkcja 3 " + name)

fun3("qw")