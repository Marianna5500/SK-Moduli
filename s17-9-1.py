import random

# Подача последовательности чисел
numbers = list(random.sample(range(1,20),10))

# Получение дополнительного числа от пользователя
user_number = int(input("Введите число от 1 до 20: "))

# Печать введенных данных
print("Введенная последовательность чисел:", numbers)
print("Дополнительное число:", user_number)

def search(testlist, value):

    if value <= testlist[0]:
        return -1
    elif value >= testlist[-1]:
        return len(testlist)-1

    lastvalue = testlist[0]
    position=0

    for index in range(len(testlist)-1):
        if lastvalue > 0 and ((value - testlist[index]) - (testlist[index+1] - value)) <= 0:
            position = index
        lastvalue = (value - testlist[index]) - (testlist[index+1] - value)

    return position


def sort_sequence(numbers):
    numbers.sort()
    return numbers


# Сортировка последовательности чисел
sorted_numbers = sort_sequence(numbers)

# Поиск позиции
position = search(sorted_numbers, user_number)

# Печать отсортированной последовательности и позиции элемента
print("Отсортированная последовательность чисел:", sorted_numbers)
print("Позиция элемента, который меньше введенного числа:", position)

