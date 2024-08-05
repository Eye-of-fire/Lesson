#name = input("Enter your name: ")
#if name == 'vadim':
#    print('Hello admin', name)
#else:
#    print('Hello', name)

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 :
    print('fizz')
elif num % 5 == 0 :
    print('buzz')
else:
    print(num)

