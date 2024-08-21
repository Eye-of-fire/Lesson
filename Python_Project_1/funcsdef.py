def print_params(a,b,c):
    print(a,b,c)
list_ = [2,3]
print_params(*list_,1)

def print_params_1(**kwargs):
    print(kwargs)
dict_ = {'a':3,'b':2,'c':1}
print_params_1(**dict_)


def print_params_2(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
    print(kwargs)
dict_ = {'a':3,'b':2,'c':1}
print_params_2(**dict_)

def print_params_3(a,b,c):
    print(a,b,c)
list_ = [2,3]
dict_ = {'c':4}
print_params_3(*list_,**dict_)