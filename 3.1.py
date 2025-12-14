summa = 0

while True:
    num = int(input("Введите число: "))

    if num == -1:
        break

    summa += num

print(f"Сумма введенных чисел: {summa}")