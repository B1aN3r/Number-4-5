katet1 = [i for i in input('Введите первые катеты a: ').split()]
katet2 = [i for i in input('Введите вторые катеты b: ').split()]

if len(katet1) != len(katet2):
    raise InconsistentDataError ('Введи одинаковое кол-во катетов')
for i in range(len(katet1)):
    if True != katet1[i].isdigit() or True != katet2[i].isdigit():      #Костыли
        raise NonNumericError ('Введи число, а не что-то другое')       #Костыли
    else:
        katet1[i] = int(katet1[i])      #Костыли, как сделать по-человечески
        katet2[i] = int(katet2[i])      #Костыли, подскажите пожалуйста, как не говнокодить??

for num in range(len(katet1)):

    sqr = [(katet1[i] * katet2[i])/2 for i in range(len(katet1))]

    hypo = [(katet1[i]**2 + katet2[i]**2)**0.5 for i in range(len(katet1))]
    hypoten = [round(i, 2) for i in hypo]

    tr = [i+1 for i in range(len(katet1))]
    print(f'Треугольник {tr[num]} с катетами {katet1[num]} и {katet2[num]} имеет площадь {sqr[num]} и гипотенузу {hypoten[num]}')
