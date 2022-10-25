a=input()
b=a.count("f")
if b==1:
    print(a.index("f"))
elif b>1:
    print(a.index("f"),a.rindex("f"))
else:
    print("-1")