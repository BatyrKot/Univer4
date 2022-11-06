import Games
import Record
def menu():
    while True:
        k=0
        print("Добро пожаловать в игру $Поле чудес$. \n Рекорд игры:",Record.checkrecord())
        print("Выберите уровень сложности: \n [1] Easy (количество жизней = 7)  \n [2] Normal (количество жизней = 5)"
              " \n [3] Hard (количество жизней = 3 ) \n [4] Legendary (количество жизней = 1) ")
        difficul=int(input())
        if difficul==1:
            Games.game(7,k)
        if difficul == 2:
            Games.game(5,k)
        if difficul == 3:
            Games.game(3,k)
        if difficul == 4:
            Games.game(1,k)