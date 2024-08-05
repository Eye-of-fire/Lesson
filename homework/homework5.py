immutable_var = (1,2,3)
print(immutable_var)
#immutable_var[0] = 2
#print(immutable_var)  ## 'tuple' object does not support item assignment
mutable_list = [1,2,3]
mutable_list[0] = 200
print(mutable_list)