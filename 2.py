def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("Конвертер температуры")
print("1. Цельсий → Фаренгейт")
print("2. Фаренгейт → Цельсий")

choice = input("Выберите направление (1 или 2): ")
temp = float(input("Введите температуру: "))

if choice == '1':
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {result:.2f}°F")
elif choice == '2':
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {result:.2f}°C")
else:
    print("Неверный выбор!")