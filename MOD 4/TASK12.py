a=int(input())
b=int(input())
if a==2:
    if b!=28:
        print(a,"-",b+1,"-","2022", sep="")
    else:
        print(a+1,"-",1,"-","2022", sep="")
else:
    if a%2==0:
        if b != 30:
            print(a, "-", b + 1, "-", "2022", sep="")
        else:
            print(b + 1, "-", 1, "-", "2022", sep="")
    if a%2==1:
        if b != 31:
            print(a, "-", b + 1, "-", "2022", sep="")
        else:
            print(a + 1, "-", 1, "-", "2022", sep="")