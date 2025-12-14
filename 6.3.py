rainfall = {
    "Январь": 45,
    "Февраль": 32,
    "Март": 38,
    "Апрель": 42,
    "Май": 55,
    "Июнь": 70,
    "Июль": 85,
    "Август": 78,
    "Сентябрь": 60,
    "Октябрь": 52,
    "Ноябрь": 48,
    "Декабрь": 44
}

print("Исходный словарь:", rainfall)

sorted_rainfall = sorted(rainfall.items(), key=lambda x: x[1])

print("\nМесяцы по возрастанию осадков:")
for month, amount in sorted_rainfall:
    print(f"{month}: {amount} мм")