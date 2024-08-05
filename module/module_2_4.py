#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#primes = []
#not_primes = []
#for i in numbers:
#    for j in numbers:
#        if i % j == 0:
#            not_primes.append(i)
#            primes.append(j)
#print(f'yes {primes},not {not_primes}')
#print('_______________________________________________________________________________________________________________')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
for i in range(2, len(numbers) + 1): #=> цикл для перебора чисел
    for j in range(2, i): #=> вложенный цикл для перебора делителей
        if i % j == 0:
            a = a + 1

    if a == 0:
        primes.append(i)
    else:
        a = 0

        not_primes.append(i)
print('primes:', primes)
print('not_primes:', not_primes)
print(range(2, len(numbers) + 1))
