def decimal_to_binary(n):
    if n == 0:
        return "0"

    bin_str = ""
    temp = n

    while temp > 0:
        rem = temp % 2
        bin_str = str(rem) + bin_str
        temp = temp // 2

    return bin_str



num = int(input("Введите десятичное число: "))
result = decimal_to_binary(num)

print(f"Исходное число: {num}")
print(f"Двоичное представление: {result}")