food = ['apple', 'orange', 'banana']  ## Списки
print(food)
print(food[0])
food[0] = 'banana'
print(food)
food.append(True)
print(food)
food.extend('string')
print(food)
food.extend(['string',2])
print(food)
food.remove('banana')
print(food)
print('banana' in food)
print('banana' not in food)
print(food[0:2:])
print()
tuple_ = 1,2,3,4,5
print(tuple_)  # Кортеж не изменяемая
tuple_2 = (1,2,3,4,5)
print(tuple_2)
tuple_4 = [1,2,3,4,5]
tuple_3 = (tuple(tuple_4))
print(tuple_3)
print(tuple_4[0])
#tuple_[0] = 200  ## 'tuple' object does not support item assignment
#print(tuple_)

tuple_ = 1,2,True,'string'
list1 = [1,2,True,'string']
print(tuple_.__sizeof__())
print(list1.__sizeof__())
print()

tuple_ = ([1,2],True,'string') + (3,4)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
tuple_ = (1,0) * 3
print(tuple_)
