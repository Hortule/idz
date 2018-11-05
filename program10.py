def opred(inp0):
    if inp0 == 'сила' or inp0 == 'здоровье' or inp0 == 'мудрость' or inp0 == 'ловкость':
        print('Вы хотите добавить очки к характеристике или забрать?')
        act(input().lower(), inp0)
    elif inp0 == 'статы':
        print(stats)
        print('кол-во очков:', points)
        opred(input('Какую стату хотите менять?\n'))
    elif inp0 == 'закрыть': 
        return None
    else:
        print('вы ввели что-то не то')
        opred(input().lower())

def act(iod, inp):
    global points
    global stats
    global count
    if iod == 'добавить' or iod == 'забрать':
        try:
            count = int(input('сколько хотите ' + iod + '\n'))
        except:
            print('попробуй сначала')
        else:
            if iod == 'забрать' and (stats[inp] - count  < 0 or stats[inp] == 0):
                print('либо очков 0, либо столько нельзя забрать')
            elif iod == 'забрать' and stats[inp] - count  >= 0 and not stats[inp] == 0:
                stats[inp] -= count
                points += count       
            elif iod == 'добавить' and points - count >= 0:
                stats[inp] += count
                points -= count
            elif iod == 'добавить' and points - count <= 0:
                print('у тебя столько нет')
            else:
                print('ты что-то сделал не так, начни сначала')
    else:
        print('тут такая команда недопустима')
    print('какую стату хотите менять?')
    print('"статы" для просмотра стат')
    print('"закрыть" для выхода')
    opred(input().lower())
    


points = 30
count = None
stats = {'сила': 0, 'здоровье': 0, 'мудрость': 0 ,'ловкость': 0}
print('Это генератор персонажей')
print('Вам доступны 30 очков и характеристики:')
print('Сила, Здоровье, Мудрость, Ловкость')
print('вы можете ввести "статы",\nчтобы узнать текущее распределение статистики')
print('Введите название статистики которую хотите изменить')
opred(input('для выхода вы всегда можете ввести "закрыть"\n').lower())
