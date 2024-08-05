name = "Denis"
print(name)
name = "Urban"
print(name)
print()
date_of_birth = "March 1999"  ## stil- Snake case
dateOfBirth = "March 1999"  ## stil- Camel case
print()
name = "Urban"
print(name,type(name)) ## Urban <class 'str'
name = 5
print(name,type(name))  ## 5 <class 'int'
name = 5.5
print(name,type(name))  ## 5.5 <class 'float'
name = [5,5]
print(name,type(name))  ## [5, 5] <class 'list'
print()
age = 25
new_age = "26"
print(age + new_age)  ## unsupported operand type(s) for +: 'int' and 'str'