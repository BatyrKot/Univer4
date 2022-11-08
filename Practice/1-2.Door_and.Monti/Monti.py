import random
def get_monti(count):
    k1=0
    k2=0
    for i in range(count):
        a=[0,1,0]
        a.pop(random.choice(a))
        if a[0]+a[1]==1:
            k1+=1
        else:
            k2+=1
    return f"Вероятность победы при смене выбора:  {k1/100} \n" \
           f"Вероятность, когда игрок не настоял на смене выбора: {k2/100}"