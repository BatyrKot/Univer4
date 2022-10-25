Ludi=int(input())
par=(Ludi*(Ludi-1))//2
God=28*12
n=God-Ludi
def factor(God):
    if God==0:
        return 1
    return factor(God-1)*God
def fact(n):
    if n==0:
        return 1
    return factor(n-1)*n
Ver=factor(God)/((God**Ludi)*fact(n))
print(factor(God),((God**Ludi)*fact(n)))