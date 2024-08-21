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




den = Human('Denis', 22)
max = Human('Maks', 22)
max.birthday()


# den.say_info()
# max.say_info()

# print(den.name, den.age)
# den.surname = 'Jack'
# den.surage = 25
# print(den.surname, den.surage)
# print(max.name, max.age)



#print(den.name, max.name)
#print (id(den), id(max))
#print(den is max)
#print(den == max)
#print(type(den))
