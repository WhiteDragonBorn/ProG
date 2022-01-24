#23 --- 106 --- KP 

targ = 34
def F(num,cnt):
    if cnt == 0:
        if num == targ:return 1
        return 0
    return (F(num+1,cnt-1) + F(num*2,cnt-1) + F(num*3,cnt-1))
print(F(1,8))#21