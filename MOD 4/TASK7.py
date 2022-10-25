a=int(input())
if a//1000==a%10 and a//100%10==a//10%10:
    print("Да")
else:
    print("Нет")