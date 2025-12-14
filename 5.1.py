def find_max_digit(number):
    """Функция принимает число и возвращает его наибольшую цифру"""
    num = str(number)
    max_digit = -1
    for char in num:
        digit = int(char)

        if digit > max_digit:
            max_digit = digit

    return max_digit

num = input("Введите число: ")
result = find_max_digit(num)

print(f"Наибольшая цифра: {result}")