listcontact= {}


def getname():
    name=input("Введите имя контакта: ")
    name=name.title()
    name=name.strip()
    return name

def trans_name(listcontact,name,num):
    if name in listcontact:
        listcontact[name] = num
        print("\nКонтакт успешно изменён\n")
    else:
        print("Такого контакта нету")
        return trans_name()

def delete_contact(listcontact,name):
    if name in listcontact:
        listcontact.pop(name)
        print("\nКонтакт успешно удалён\n")
    else:
        print("Такого контакта нету")

def get_num():
    num=input("Введите номер телефона: ")
    num=num.replace(" ","").replace("-","")
    if num[0]=="9" and len(num)==10:
        num="+7"+num
        return num
    if num[0]=="8" and len(num)==11:
        num = "+7" + num[1:]
        return num
    if num[0]=="7" and len(num)==11:
        num = "+" + num
        return num
    if num[:2]=="+7" and len(num)==12:
        return num
    else:
        print("Неправильно набран номер\n")
        return get_num()

def get_contact(listcontact,name,num):
    listcontact[name]=num
    print("Контакт успешно добавлен\n")
    return listcontact

def show_contact(listcontact):
    print("Список контактов: ")
    for i in listcontact:
        print(i, listcontact[i])

def menu():
    print("Выберите действие: \n 1.Добавить Контакт \n 2.Показать контакты \n 3.Удалить контакт \n"
          " 4.Изменить номер \n 5.Выход")

while True:
    menu()
    p=int(input())
    if p==1:
        get_contact(listcontact,getname(),get_num())
    if p==2:
        show_contact(listcontact)
    if p==3:
        delete_contact(listcontact,getname())
    if p==4:
        trans_name(listcontact,getname(),get_num())
    if p==5:
        print("Спасибо за использование")
        break