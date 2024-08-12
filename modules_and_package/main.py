# import random
# print(random.randint(1, 100))  # импротирует всю библиотеку
# from random import randint
# print(randint(1,100))  # импортирует только randint
# import test
# print(test.x)
# test.test_func(2)

# from test import x
# from test import test_func as new_test_func
# print(x)
# print(new_test_func(x))
#
# def test_func(num):
#     print('test_func main.py')
#
# test_func(1)

# import tests
# from tests import test
from tests.test import x
# print(x)