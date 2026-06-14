# Список — это коллекция элементов в определённом порядке
fruits = ["яблоко", "банан", "апельсин", "манго"]

print(fruits)  # Выводим весь список
print(fruits[0])  # Выводим первый элемент индекс всегда с нуля
print(fruits[1])  # Выводим второй элемент
print(fruits[2])  # Выводим третий элемент

print(len(fruits))  # Длина списка

# Изменение элемента списка
fruits[1] = "виноград"
print(fruits)

# Добавление элемента в конец
fruits.append("клубника")
print(fruits)

# Удаление элемента
fruits.remove("яблоко")
print(fruits)

# Есть ли элемент в списке
print("манго" in fruits)  # True
print("яблоко" in fruits)  # False

# Проходим по каждому элементу списка
fruits = ["яблоко", "банан", "апельсин", "манго"]

for fruit in fruits:
    print(f"Фрукт: {fruit}")

print("---")

# for с числами - range()
for i in range(5):
    print(i)  # Выводит числа от 0 до 4

print("---")

#range(start, stop, step)
for i in range(1, 11, 2):
    print(i)  # Выводит нечетные числа от 1 до 9

print("---")

# Считаем сумму чисел в списке
numbers = [10, 25, 3, 47, 15]
total = 0

for num in numbers:
    total += num # total = total + num

print(f"Сумма чисел: {total}")
print(f"Среднее значение: {total / len(numbers)}")

def find_max(numbers):
    max_num = numbers[0]  # Предполагаем, что первый элемент - максимум
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
numbers = [10, 25, 3, 47, 15]
print(find_max(numbers))





