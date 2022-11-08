import random
def get_birthday(ludi):
    gr=1000
    count = 0
    for i in range(gr):
        sp=[]
        for p in range(ludi):
            sp.append(random.randint(1,364))
        if len(set(sp))!=ludi:
            count +=1
    return f"""Вероятность того, что нам надо: {count / (gr / 100)} \n"""
