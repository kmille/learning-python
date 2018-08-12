from ipdb import set_trace

def my_decorator(func):
    def wrapper(*args, **kwargs):
        #print("Calling {} with args {} and kwargs {}".format(func.__name__, args, kwargs))
        print("Calling {} with args {}".format(func.__name__, locals()))
        func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function(what):
    print("hi", what)

my_function("banane")
"""
    1. call my_decorator(my_function)
    2. call wrapper("banane")
    3.   print("Calling ...")
    4.   call(my_function("banane")
"""

#my_decorator(my_function)("banane") # this works if you comment out the my_decorator


def my_decorator_with_parameter(*args2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Calling {} with args {} and kwargs {}".format(func.__name__, args, kwargs))
            func(*args, **kwargs)
            print("after")
        return wrapper
    return decorator


@my_decorator_with_parameter('birne', 'apfel')
def my_function2(what):
    print("hi ho", what)

my_function2("birne")

"""
    1. call my_decorator_with_parameter('birne', 'apfel')
    2. call decorator(my_decorator_with_parameter('birne', 'apfel'))
    3. call wrapper(decorator(my_decorator_with_parameter('birne', 'apfel'))
"""
