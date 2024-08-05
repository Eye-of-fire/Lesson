a = [True,False,False]
print(any(a))
print('-----1------')
a = [False,False,False]
print(any(a))
print('-----2------')
a = [1,0,0]
print(any(a))
print('-----3------')
a = [0,0,0]
print(any(a))
print('-----4------')
b = '0'
print(any(b))
print('-----5------')
a = [True,False,False]
print(all(a))
print('-----6------')
a = [True,True,True]
print(all(a))
print('----7------')
a = [True,False,False]
print(dir(a))
print('----8------')
b = '0'
print(isinstance(b,str))
print('----9------')

a = [1,2,3]
d = [1,2,3]
c = d
print(id(a))
print(id(d))
print(id(c))
print(a == d)
print(a is d)
#print(help(a))

def helper():
    """
    эта функция помошник

    """
    pass
#print(help(helper))
print(helper.__doc__)