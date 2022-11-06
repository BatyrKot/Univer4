

def record(record):
    text = open("Rec.txt", mode='w+')
    text.write(record)
    text.close()
def checkrecord():
    text=open("Rec.txt", "r", encoding="utf-8")
    text=int(text.read())
    return text
