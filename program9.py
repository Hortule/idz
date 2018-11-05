import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
# pick one word randomly from the sequence
word = random.choice(WORDS)

# start the game
print(
"""
ты должен отгдадать слово
можешь пять раз спросить о наличии буквы
или отгадать сразу
"""
)
i = 5
ind = False
while i > 0 :
    print('''   угадай слово или спроси букву
    ты можешь спросить еще: 
    ''', i, ' букв')
    inpw = input()
    if inpw == word:
        print('you win')
        ind = True
        i = 0
        break
    elif len(inpw) != 1:
        print('ты либо не угадал\nлибо спросил больше одной буквы,\nпопытка затрачена')
    elif inpw in word:
        print('YES')
    else: print('NO')
    i -=1
if ind == False:
    if i == 0:
        inpw = input('your last chanse\n')
    if inpw == word:
        print('you win')
    else: print('you lose')
    

    
print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
