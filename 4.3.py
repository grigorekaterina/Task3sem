height = int(input("Введите высоту елки: "))
symbol = input("Введите символ: ")

for i in range(height - 1):
    spaces = " " * (height - 2 - i)
    branch = symbol * i

    print(f"{spaces}{branch}||{branch}")

base_spaces = " " * (height - 2)
print(f"{base_spaces}||")