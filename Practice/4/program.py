

def read_file(file):
    text=open(file, 'r', encoding="utf-8").read().lower()
    words=text.split()
    words=[word.strip('.,!;()[]-+=—') for word in words]
    uniq=[]
    for word in words:
        if word not in uniq:
            uniq.append(word)
    return uniq

def save_file(uniq):
    text = open("count.txt", mode='w+')
    vsego=len(uniq)
    text.write(f"{str(vsego)} \n {uniq}")
    uniq.sort()
    spisk="\n".join(uniq)
    return f"""Всего уникальных слов: {vsego}\n========================\n{spisk} """




