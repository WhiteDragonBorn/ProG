# 23 --- 15834 --- RE

def F(start,res):
    if start > res:
        return 0
    if start == res:
        return 1
    if start == 31:
        return 0
    return F(start+1,res) + F(start*2,res)
print(F(2,15)*F(15,35)) # 26
