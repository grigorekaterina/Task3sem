num = input("Введите натуральное число: ")

max_digit = -1

for char in num:
    digit = int(char)

    if digit > max_digit:
        max_digit = digit

print(f"В числе {num} наибольшая цифра: {max_digit}")