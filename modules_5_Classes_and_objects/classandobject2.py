class Human:
    def __init__(self, name, age):
        self.name = name  #'Den'
        self.age = age
        self.say_info()
    def say_info(self):
        print(f'Привет, меня зовут {self.name},мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')

    def __del__(self):
        print(f'{self.name} ушел')

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __str__(self):
        return f'{self.name}'

den = Human('Denis', 22)
max = Human('Maks', 22)
a = 6
print(den)
print(max)

# max.name = 'Denis'
# #__lt__
# print(den < max)
#
# #__gt__
# print(den > max)
#
# #__eq__
# print(den == max)
#
# if den :
#    den.say_info()
#
# max.birthday()
#
# #__gt__
# print(max > den)
#
# #__lt__
# print(den < max)
#
# #__eq__
# print(max == den)