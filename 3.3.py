import random

secret_number = random.randint(1, 10)
attempts = 3
flag = False

for i in range(attempts):
    print(f"Попытка № {i + 1}")
    num = int(input("Ваше число: "))

    if num == secret_number:
        print("Поздравляю! Вы угадали!")
        flag = True
        break
    elif num < secret_number:
        print("Мое число БОЛЬШЕ")
    else:
        print("Мое число МЕНЬШЕ")

if not flag:
    print(f"Увы, попытки закончились. Я загадал число {secret_number}")