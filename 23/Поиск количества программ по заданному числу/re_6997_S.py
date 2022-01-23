# 23 --- 6997 --- RE

def F(num,trg):
    if num == trg: 
        return 1
    elif num > trg:
        return 0
    return (F(num+1,trg)+ F(num*2,trg)+ F(num*2+1,trg)+ F(num*10,trg))
print (F(1,15)) #84