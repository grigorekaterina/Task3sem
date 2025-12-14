print("Выберите режим перевода:")
print("1 - Цельсий -> Фаренгейт")
print("2 - Фаренгейт -> Цельсий")

choice = input("Ваш выбор (1 или 2): ")

if choice == "1":
    cels = float(input("Введите температуру в градусах Цельсия: "))
    far = cels * 1.8 + 32
    print(f"{cels}°C = {far}°F")

elif choice == "2":
    far = float(input("Введите температуру в градусах Фаренгейта: "))
    cels = (far - 32) / 1.8
    print(f"{far}°F = {round(cels, 2)}°C")

else:
    print("Нужно ввести 1 или 2")