age = int(input("Сколько тебе лет? "))

if age > 18:
    print("Ты совершеннолетний!")
elif age == 14:
    print("Ты подросток")
else:
    print("Ты ребенок")


number = int(input("Введите число от 1 до 10: "))

if number < 1 or number > 10:
    print("Это не число от 1 до 10")
elif number >= 7:
    print("Счастливое число!")
else:
    print(f"Ты ввел {number}")



