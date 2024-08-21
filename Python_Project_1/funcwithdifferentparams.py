print('-------------------------------------0--------------------------------------------------')
def test_func(*params):
     print("Тип:", type(params))
     print("Аргумент:", params)
     #print(params)

test_func(1, 2, 3, 4)

print('-------------------------------------1--------------------------------------------------')
def summator(txt, *values, type="sum"):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s} {type}'



print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))

print('-------------------------------------2--------------------------------------------------')


def info(value, *types, names_author="Den", **values):
    print("Тип:", type(values))
    print("Аргумент:", values)
    for key, value in values.items():
        print(key, value)
    print(types)


info("Пример использования параметров всех типов", 2, 3, 4, names_author="Denis", name="Den", course="Python")

print('-------------------------------------3--------------------------------------------------')
def my_sum(n, *args, txt="Сумма чисел"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)


my_sum(1,  2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")
print('-------------------------------------4--------------------------------------------------')
def info( **values):
    print("Тип:", type(values))
    print("Аргумент:", values)
    for key, value in values.items():
        print(key, value)



info( names_author="Denis", name="Den", course="Python")