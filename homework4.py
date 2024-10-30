import random
x = input("Введите число X: ")
if x.isdigit():
  x1 = int(x)
  numbers = random.sample(range(0, 201), 20)
  d= [num for num in numbers if num % x1 == 0]
  print("Сгенерированный список чисел:", numbers)
  if d:
    print("Числа, кратные X:", d)
  else:
    print('В списке нет чисел, кратных X.')
else:
  print("Ошибка! Введите целое число.")
