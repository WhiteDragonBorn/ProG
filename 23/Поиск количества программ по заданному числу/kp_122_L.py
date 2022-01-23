# 23 --- 122 --- KP

def F(start,res):
    if start > res:
        return 0
    if start == res:
        return 1
    return F(start+2,res) + F(start+4,res) + F(start+5,res)

for x in range(32,61):
    if int(F(31,x)) == 1001:
        print(x) # 56
