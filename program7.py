from random import randint
a = randint(0, 11)
city = ('Сергиев Посад', 'Переславль-Залесский', 'Ростов Великий', 'Ярославль', 'Кострома', 'Иваново', 'Суздаль', 'Владимир', 'Александров', 'Боголюбов', 'Гороховец', 'Гусь-Хрустальный')
print('ugaday odin iz etih: ', city)
print('test', city[a])
b = input('vvodi ')
points = 12
for i in range(0, 12):
    if b == city[a]:
        print('you win')
        break
    else:
        b = input('vvodi ')
        points -= 1
if i == 11:
    print('you lose')
print('count of your points: ', points)
input('press enter to close')
