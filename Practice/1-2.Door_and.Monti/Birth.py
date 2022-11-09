import random
def get_birthday(gr,ludi=28):
    count = 0
    for i in range(gr):
        sp=[]
        for p in range(ludi):
            sp.append(random.randint(1,364))
        if len(set(sp))!=ludi:
            count +=1
    return f"""Парадокс произошел в: {count / (gr / 100)}% \n"""
