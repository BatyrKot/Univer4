import Slovo
import Record
def end():
    print("Желаете начать заново, чтобы побить рекорд ? \n [1] Начать заново \n [2] Закончить")
    p=int(input())
    if p==1:
        Slovo.get_text(Slovo.word)
        return True
    if p==2:
        exit()
def game(lives,k):
    if not Slovo.word:
        print("Игра окончена, у меня закончились слова")
        return end()
    slovox=Slovo.get_slovo(Slovo.word)
    shifrx=Slovo.get_shifr(slovox)
    relives=lives
    while lives>0:
        if shifrx==slovox:
            print(f"You win! Загаданное слово: {slovox}")
            return regame(relives,k)

        print(f"{shifrx} | {'❤' * lives}")
        check=input("Введите букву или слово целиком: ").upper()

        if check==slovox:
            print("You win!")
            return regame(relives,k)
        if len(check)!=1:
            print("Ошибочка, у вас отнимается жизнь")
            lives-=1
            continue
        if check in slovox:
            print("Такая буква есть!")
            shifrs=list(shifrx)
            shifrs[slovox.index(check)]=check
            shifrx=''.join(shifrs)
            continue
        if check not in slovox:
            print("Ошибочка, у вас отнимается жизнь")
            lives -= 1
            continue
def regame(relives,k):
    print("Вы прошли данный тур, если хотите продолжить, напишите [1] \n [2] Если устали, и хотите закончить")
    recont=int(input())
    k+=1
    print("Ваш текущий рекорд: ",k)
    if k>Record.checkrecord():
        Record.record(str(k))
    if recont==1:
        lives=relives
        return game(lives,k)
    if recont==2:
        exit()
    else:
        return True