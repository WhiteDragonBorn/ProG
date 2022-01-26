#23 --- 128 --- KP

def F(num,trg):
    if num == 43:
        return 0
    if num == trg:
        return 1
    elif num > trg:
        return 0

    return (F(num+2,trg)+F(num+num-1,trg)+F(num + num+1,trg))
print (F(7,63))#116