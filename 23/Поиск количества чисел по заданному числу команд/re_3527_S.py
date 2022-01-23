# 23 --- 3527 --- RE

def F(num,cnt):
    global mas
    if cnt == 0:
        if num in mas:
            return 0
        mas.append(num)
        return 1
    return (F(num*8,cnt-1)+F(num/2,cnt-1))
mas = []
print(F(512,8))#9