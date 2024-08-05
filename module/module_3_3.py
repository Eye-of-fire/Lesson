def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [250, 'Строка',False ]
values_dict = {'a' : 100,'b' : 200,'c' : 300}
values_list_2 = [54.32, 'Строка' ]


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

values_list = (1,2,)
values_dict = {'c':3}
print_params(*values_list, **values_dict)