from collections import Counter

jurnal = [ 
    {'name': 'Anna', 'age': 25, 'gender': 'female'},
    {'name': 'Lena', 'age': 12, 'gender': 'female'},
    {'name': 'Nastya', 'age': 33, 'gender': 'female'},
    {'name': 'Angelina', 'age': 30, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Anna', 'age': 40, 'gender': 'female'},
    {'name': 'Ira', 'age': 11, 'gender': 'female'},
    {'name': 'Polina', 'age': 17, 'gender': 'female'},
    {'name': 'Oksana', 'age': 18, 'gender': 'female'},
    {'name': 'Anna', 'age': 8, 'gender': 'female'},
    {'name': 'Yana', 'age': 43, 'gender': 'female'},
    {'name': 'Kira', 'age': 18, 'gender': 'female'},
    {'name': 'Nastya', 'age': 25, 'gender': 'female'},
    {'name': 'Tamara', 'age': 31, 'gender': 'female'},
    {'name': 'Rita', 'age': 39, 'gender': 'female'},
    {'name': 'Sveta', 'age': 25, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Nastya', 'age': 28, 'gender': 'female'},
    {'name': 'Lera', 'age': 19, 'gender': 'female'},
    {'name': 'Sara', 'age': 10, 'gender': 'female'},
    {'name': 'Filya', 'age': 44, 'gender': 'male'},
    {'name': 'Dima', 'age': 33, 'gender': 'male'},
    {'name': 'Fedor', 'age': 38, 'gender': 'male'},
    {'name': 'Nikita', 'age': 32, 'gender': 'male'},
    {'name': 'Alex', 'age': 25, 'gender': 'male'},
    {'name': 'Foma', 'age': 7, 'gender': 'male'},
    {'name': 'Evgeniy', 'age': 25, 'gender': 'male'},
    {'name': 'Alex', 'age': 12, 'gender': 'male'},
    {'name': 'Kiril', 'age': 27, 'gender': 'male'},
    {'name': 'Mihail', 'age': 30, 'gender': 'male'}
]
#Выводит общее количество людей в журнале
#num = len(jurnal)
#print(f'Количество всех людей в журнале: {num}')

#Выводит общее количество мужчин и девушек в журнале
gn = [gn['gender'] for gn in jurnal]
mn = gn.count('male')
wmn = gn.count('female')
#print(f'Количество мужчин: {mn}, и количество девушек: {wmn}')

#Выводит общее количество совершеннолетних в журнале
ages = [gn['age'] for gn in jurnal]
ag = ([ag for ag in ages if ag > 17])
ag = len(ag)
#print(f'Количество совершеннолетних людей в журнале: {ag}')

#Выводит список имен в журнале
names = [print(gn['name']) for gn in jurnal]

#Выводит множество возрастов
ages = [gn['age'] for gn in jurnal]
no_repeat = set(ages)
#print(no_repeat)

#Выводит 3 наиболее встречающихся имени в журнале
namess = Counter([gn['name'] for gn in jurnal])
#print(namess.most_common(3))

#Выводит мужчин страше 35 и с именем на 'F'
#for i in jurnal:
  #  if i['age'] > 34:
      #  if i['name'][0] == "F":
          #  if i['gender'] == 'male':
          #      print(i['name'])
          