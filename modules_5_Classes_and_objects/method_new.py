class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,*args,**kwargs):
        print('Я в инете')
        self.args = args
        for key, values in kwargs.items():
            setattr(self,key,values)


other = [1,2,3]
user = {'name': 'Den', 'age': 25,'gender':'male'}


user1 = User(*other,**user)
print(user1.name)
print(user1.age)
print(user1.gender)
# user2 = User
()# print(User.__mro__)
# print(user1)
# print(user1 is user2)
# print(id(user1), id(user2))