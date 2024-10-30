import random
def game():
  a = 0
  b = 0
  while a < 3 and b < 3:
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ")
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice.lower() in choices:
      if user_choice == computer_choice:
        print("Ничья!")
      elif (user_choice == "камень" and computer_choice == "ножницы") or \
           (user_choice == "ножницы" and computer_choice == "бумага") or \
           (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
        a += 1
      else:
        print("Вы проиграли!")
        b += 1
    else:
      print("Некорректный ввод! Введите 'камень', 'ножницы' или 'бумага'.")
    print(f"Счет: Вы - {a}, Компьютер - {b}")
  if a == 3:
    print("Поздравляю, вы победили в игре!")
  else:
    print("К сожалению, компьютер победил.")
game()


