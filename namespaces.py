from math import *
# def print(*args):
#     return 'ok'
d = 5
def square(x):
    # global a
    # a = x ** 2
    # print(globals())
    # print(locals())
    # d = x ** 2
    def even (x):
        # d = x * 2
        if d % 2 == 0:
            print('четное')
        else:
            print('нечетное')
    even(x)
    return d

a = 5
b = square(4)
# print(sqrt(a))
print(a)
print(b)
# print(d)
# print(globals())