# 23 --- 35997 --- RE

def F(num,rem):
    if rem == 0:
        return 1
    
    return F(num*2, rem-1) + F(num*2+1, rem-1)

print(F(1,10)) # 1024
