phone_book = {'Denis': '89991642352', 'Vadim': '89991647672'}  ## Словарь
print(phone_book)
print(phone_book['Vadim'])
phone_book['Denis'] = 123456789
phone_book['Anton'] = 987456123
del phone_book['Vadim']
phone_book.update({'sasha':123456789,'alex':987456123})
print(phone_book)
print()
print(phone_book.get('sasha'))
print(phone_book.get('katya','net katya'))
a = phone_book.pop('Denis')
print(a)
list_ = [1,2,3,4,5,6,7,8,9,10]
list_.pop(0)
print(list_)
print()

print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())
print()

set_ = {1,2,3,1,2,3,'string',True,'string'}
print(set_)
list_ = [1,2,3,4,5,5,4,3,2,1]
print(set(list_))
list_ = set(list_)
print(list_)
print(list_.discard(2))  # не выдает ощибку если нет обьекта
print(list_.remove(1))
print(list_.add(9))
print(list_)
print()

from time import sleep
a = 5
print(a)
print('я тут')
sleep(4)
print('фух, 4 секуды прошло')