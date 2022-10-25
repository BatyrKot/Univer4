test={}
def name():
    name=input()
    return name
def num():
    num=input()
    return num
def sum(test,num,name):
    test[name]=num
    print(test,name,num)
while True:
    Type=int(input())
    if Type==1:
        sum(test,name(),num())
    if Type==2:
        print(test)