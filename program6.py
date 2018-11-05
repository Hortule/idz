from random import randint
a = randint(0, 11)
city = ('Сергиев Посад', 'Переславль-Залесский', 'Ростов Великий', 'Ярославль', 'Кострома', 'Иваново', 'Суздаль', 'Владимир', 'Александров', 'Боголюбов', 'Гороховец', 'Гусь-Хрустальный')
print('ugaday odin iz etih: ', city)
b = input('vvodi ')
if b == city[a]:
    print('you win')
else:
    print('you lose')
input('press enter to close')
