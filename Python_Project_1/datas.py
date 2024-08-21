print(5)
print(type(5))  # int -integer
print("плюс 5+5=",5+5)
print("минус 5-5=",5-5)
print("умножить 5*5=",5*5)
print("деление обычное 5/5=",5/5)
print("деление целочисленное 5//5=",5//5)
print("остаток 5%5=",5%5)
print("возведение степень 5**5=",5**5)

print(type(2.0))  # тип Float
print(2.0+2)
    ## числа не изменяемые данные
print()
print('числа не изменяемые данные!!!')
print("Hello World")
print(type("Hello World"))  # тип string - строка
print()
    ## concatenate это сложение
print('concatenate это сложение!!!')
print('Hello'+'world')
print('1'+'1')  # не сложение так как str
print(1+1)
print()
print('логический тип boolean')
print(True,False)
print(type(True),type(False))  # тип Bool
print(5>10)  # false лож
print(10>5)  # True правда
print(1,2,3,4,'hello world',True)
print()
print(5 >= 5, 5 <= 5, 5 ==5, 5 != 5)
print(5 != 5 and 5 < 10 ) # 5 не равен 5, 5 меньше 10 значит False  @ строгий оператор ' and '
print(5 == 5 and 5 < 10 ) # 5  равен 5, 5 меньше 10 значит True
print(5 == 5 or 5 < 10 ) # обе части верны 5  равен 5, 5 меньше 10 значит True
print(5 != 5 or 5 < 10 ) # 5 не равен 5, 5 меньше 10 значит False  @ не строгий оператор ' or '
print()
print('перевод с одного типа на другой')
print(type('1'))  ##  Tip STR
print(int('1'))  # '1' со строки на числовой
print(type(int('1')))  ## Tip INT
print()
print('Задача')
print('1st program')
print(5*((9**0.5)))
print('2st program')
print(9.99 > 9.98 or 1000 != 1000.1)
print('3st program')
a = (1234%1000)//10
b = (5678%1000)//10
c = (a + b + 23 + 67 )//4
print(c)
print()
print('4st program')
a = 13.42
b = 42.13
