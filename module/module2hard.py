def code(number):
  result = []
  for i in range(1, number + 1):
    for j in range(i +1, number + 1 ):
      sum_ = i + j
      if number % sum_ == 0:
        result.append(i)
        result.append(j)
  return result
number = int(input('Введите шифр от 3 до 20: '))
result = code(number)
print("Пароль:",*result, sep='')