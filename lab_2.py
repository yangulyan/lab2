height = float(input("Введите Ваш рост: "))
weight = float(input("Введите Ваш вес: "))
steps = float(input("Введите Ваше количество шагов: "))
time = float(input("Введите Ваше время в движении: "))
norm = float(input("Введите норму километража на сегодня: "))
length = (height / 4) + 0.37
k = length * steps
v = k / (time * 60)
calories = 0.035 * weight + (v ** 2) / height * 0.029 * weight
k = round(k, 2)
calories = round(calories, 2)
print(f'Пройденная дистанция : {k}')
print(f'Кол-во сожженных калорий в минуту : {calories}')
print(f'Кол-во пройденных км : {k / 1000}')
if k / 1000 < norm:
    print(f'Вы прошли меньше нормы, необходимо пройти ещё {round(norm-k/1000, 2)} км.!')
else:
    print('Вы прошли сегодняшнюю норму, Вы большой молодец!')
