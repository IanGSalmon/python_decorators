from functools import wraps
# A decorator is a function that returns a function
# which in turn returns a function that was accepted
# by the outermost function

# Outer, is a function that calls another function, inner
def outer():
    number = 5
    # inner only has access to number == 5
    def inner():
        print(number)

    inner()


def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

# Here we use a function as an argument
#print(apply(add, 5, 5))
#print(apply(sub, 2, 8))


# Example of a closure function
def close():
    x = 5
    def inner():
        print(x)
    # Not returning what happens when we CALL inner
    # Only returning inner
    return inner

#closure = close()
#closure()

def add_to_five(num):
    def inner():
        print(num+5)
    return inner

#fifteen = add_to_five(10)
#fifteen()


#def logme(func):
#    import logging
#    logging.basicConfig(level=logging.DEBUG)

#    def inner():
#        logging.debug("Called {}".format(func.__name__))
#        return func()
#    return inner

# In shell
# >>>def print(2):
# >>>    print(2)
# >>>print_2 = logme(print_2)
# >>>print_2()
# DEBUG:root:Called print_2
# 2

# OR, you can use @
# In shell
# >>>@logme
# ...def print_4():
# ...    print(4)
# ...
# >>>print_4()
# DEBUG:root:Called print_4
# 4

# What if we want to decorate a function that accepts arguments
# We have to change our decorator to accept the arguments
# Decorator still only takes the function
# Our inner function takes args and kwargs
def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    # If we call doc or name, it references inner
    # Set to outer argument to correct
    #inner.__doc__ = func.__doc__
    #inner.__name__ = func.__name__
    # Easier to import functools.wraps (see ln 88)
    return inner

# In shell
# from dec import logme
# >>> @logme
# ... def sub(x, y, switch=False):
# ...    return x-y if not switch else y - x
# ...
# >>> sub(5, 2)
# DEBUG:root:Called sub with args (5, 2) and kwargs {}
# 3
# >>> sub(5, 2, switch=True)
# DEBUG: root: Called sub with args (5, 2) and kwargs {'switch': True}
# -3