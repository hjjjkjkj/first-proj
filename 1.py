import random
import string

def generate_password(length=12):
    # Все возможные символы: буквы (верх/нижн), цифры, спецсимволы
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Пример использования
password = generate_password(16)
print(f"Ваш пароль: {password}")

afkj