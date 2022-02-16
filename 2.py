katet1 = [int(i) for i in input('Введите первые катеты a: ').split()]
katet2 = [int(i) for i in input('Введите вторые катеты b: ').split()]

zip_katet = list(zip(katet1, katet2))
print('Количество твоих треугольников = ', len(zip_katet))

treugolnik = int(input('Выбери номер треугольника, для взаимодействия: '))

if treugolnik <= 0 or treugolnik > len(zip_katet):
    raise IndexError('Введи номер треугольника в заданных тобой пределах!')

tr = zip_katet[treugolnik - 1]  #Получаем  кортеж  с данными нужного нам треугольника

a = tr[0]
b = tr[1]

Square = (a * b) / 2
hypo = round(((a**2 + b**2)**0.5), 2)

print(f'Треугольник {treugolnik} с катетами {a} и {b} имеет площадь {Square} и гипотенузу {hypo}')
