# Словарь — хранит данные в формате ключ: значение
user = {
    "name": "Егор",
    "age": 24,
    "city": "Ярославль",
    "is_active": True
}

# Получить значение по ключу
print(user["name"])
print(user["age"])

# изменить значение по ключу
user["age"] = 25
print(user["age"])

# добавить новый ключ и значение
user ["job"] = "Программист"
print(user)

# проверить есть ли ключ
print ("city" in user)  # True
print ("salary" in user)  # False

# перебрать все пары ключ-значение
for key, value in user.items():
    print(f"{key}: {value}")