import random

word=[]

def get_text(word):
    text = open("Word.txt", "r", encoding="utf-8")
    text = text.read().split(", ")
    text = [i.upper() for i in text]
    word+=text
    return word
def get_shifr(slovo):
    shifr="❌"*len(slovo)
    return shifr

def get_slovo(word):
    slovo = random.choice(word)
    word.remove(slovo)
    return slovo
get_text(word)