# --- 35997 --- RE

def F(num,cnt):
    global mas
    if cnt == 0:
        if num in mas:
            return 0 
        return 1
       
    return F(num*2,cnt-1)+F(num*2 + 1,cnt-1)
        
mas = []
print(F(1,10)) #1024