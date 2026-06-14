name = input("Как тебя зовут? ")
age = input("Сколько тебе лет? ")

print(f"Привет, {name}!")
print(f"Тебе {age} лет!")

year = int(input("В каком году ты родился? "))
current_year = 2026
age_calculated = current_year - year

print(f"Твой возраст по расчету: {age_calculated} лет.")
