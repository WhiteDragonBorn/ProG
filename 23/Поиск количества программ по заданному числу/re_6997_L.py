# 23 --- 6997 --- RE

def F(num,res):
    if num > res:
        return 0
    if num == res:
        return 1
    return ( F(num+1,res) + F(num*2,res) +
             F(num*2+1,res) + F(num*10,res) )
print(F(1,15)) # 84
