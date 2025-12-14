lucky_numbers = [7, 13, 21, 42, 99]

user_num = int(input("Введите число: "))

if user_num in lucky_numbers:
    print(f"Поздравляю! Число {user_num} есть в списке!")
else:
    print("Нет такого числа в списке")