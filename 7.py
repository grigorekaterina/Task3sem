group_number = input("Введите номер вашей группы: ")
filename = f"{group_number}.txt"

print(f"Данные будут записаны в файл: {filename}")
print("--- Начало ввода данных ---")


with open(filename, "w", encoding="utf-8") as file:
    while True:
        surname = input("Введите фамилию студента: ")
        address = input("Введите почтовый адрес: ")

        line = f"{surname} - {address}\n"

        file.write(line)

        choice = input("Добавить еще студента? (да/нет): ").lower()
        if choice != "да" and choice != "yes":
            break

print("\n--- Запись завершена. Чтение данных из файла... ---")


with open(filename, encoding="UTF-8") as file:
    content = file.read()

    print(f"Содержимое файла {filename}:")
    print(content)