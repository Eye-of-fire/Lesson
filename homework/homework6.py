my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Vasya'])

print(my_dict.get('Petya'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print(my_dict)
del my_dict['Kamila']
print(my_dict)

my_set = {1, 'Яблоко', 42.314,1, 'Яблоко', 42.314}
print(my_set)
my_set.add(5)
my_set.add(1.5)
print(my_set)
my_set.remove(42.314)
