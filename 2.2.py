code = int(input("Введите код символа: "))

if (65 <= code <= 90) or (97 <= code <= 122):
    print(f"Код {code} соответствует английской букве '{chr(code)}'")
else:
    print(f"Код {code} какой-то иной символ ('{chr(code)}')")