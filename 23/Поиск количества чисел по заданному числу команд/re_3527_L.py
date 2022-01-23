# 23 --- 3527 --- RE
mas = []
def F(num,res):
    global mas
    if res == 0:
        if num in mas: return 0
        
        mas.append(num) # Чтобы различные были
        return 1

    
    return F(num*2,res-1) + F(num//2,res-1)
print(F(512,8))
