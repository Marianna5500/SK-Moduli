# (C) Марианна Акулова
# Задание 13.8.19

tickets = int(input("Укажите количество приобретаемых билетов: "))
ages = input("Укажите через пробел возраст посетителей: ").strip()
cost = 0

for age in ages.split(" "):
    age = int(age)
    if age < 18:
        continue
    if age > 24:
        cost = cost + 1390
        continue
    cost = cost + 990

if tickets > 3:
    print("Применилась скидка %10")
    cost = cost * 0.9

print("Сумма к оплате:", cost)
