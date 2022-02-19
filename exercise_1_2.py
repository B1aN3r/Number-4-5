katet = [i for i in input('Введите значения катетов ').split()]

if len(katet) % 2 == 1:
    raise InconsistentDataError ('Введи четное кол-во катетов')
for i in range(len(katet)):
    if True != katet[i].isdigit():      #Костыли
        raise NonNumericError ('Введи число, а не что-то другое')       #Костыли
    else:
        katet[i] = int(katet[i])      #Костыли, как сделать по-человечески
   #Костыли, подскажите пожалуйста, как не говнокодить??

for num in range(1, (int(len(katet)/2) + 1)):

    sqr = [(katet[i] * katet[i+1])/2 for i in range(0, len(katet), 2)]

    hypo = [(katet[i]**2 + katet[i+1]**2)**0.5 for i in range(0, len(katet), 2)]
    hypoten = [round(i, 2) for i in hypo]

    print(f'Треугольник {[num]} с катетами {katet[(num-1)*2]} и {katet[(num-1)*2+1]} имеет площадь {sqr[num-1]} и гипотенузу {hypoten[num-1]} ')
