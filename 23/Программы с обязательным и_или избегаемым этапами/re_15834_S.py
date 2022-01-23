# 23 --- 15834 --- RE

def F(num,tar):
    if num == tar:
        return 1
    elif num > tar:
        return 0
    if num == 31:
        return 0
    return F(num+1,tar) + F(num*2,tar)
print (F(2,15)*F(15,35)) # 26
