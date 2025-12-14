import math

def area_rectangle(a, b):
    return a * b

def area_circle(r):
    return math.pi * (r ** 2)

def area_triangle(b, h):
    return 0.5 * b * h

print("1 - прямоугольник")
print("2 - круг")
print("3 - треугольник")

choice = input("Выберите фигуру (1/2/3): ")

if choice == "1":
    w = float(input("Введите ширину: "))
    h = float(input("Введите высоту: "))
    print(f"Площадь прямоугольника: {area_rectangle(w, h):.2f}")

elif choice == "2":
    r = float(input("Введите радиус: "))
    print(f"Площадь круга: {area_circle(r):.2f}")

elif choice == "3":
    b = float(input("Введите основание: "))
    h = float(input("Введите высоту: "))
    print(f"Площадь треугольника: {area_triangle(b, h):.2f}")

else:
    print("Неверный выбор.")