def great(name):
    message = f"Привет, {name}! Добро пожаловать!"
    return message

result = great("Егор")
print(result)

print(great("Алексей"))
print(great("Мария"))

def calculate_age(birth_year):
    age = 2026 - birth_year
    return age

def is_adult(age):
    if age >=18:
        return True
    else:
        return False

year = int(input("Введите год рождения: "))
age = calculate_age(year)
adult = is_adult(age)

print(f"Тебе {age} лет.")
if adult:
    print("Ты совершеннолетний.")
else:
    print("Ты несовершеннолетний.")