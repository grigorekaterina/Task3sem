n = int(input("Введите число n: "))

summa = 0
fact = 1

for i in range(1, n + 1):
    fact=fact*i
    summa = summa + fact

print(f"Сумма факториалов от 1! до {n}! = {summa}")