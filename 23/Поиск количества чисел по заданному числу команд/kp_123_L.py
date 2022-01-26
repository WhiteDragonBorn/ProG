# 23 --- 123 --- KP
def F(num,rem):
    if rem == 0:
        if num == 80: return 1
        return 0
    
    return F(num+1,rem-1) + F(num*2,rem-1) + F(num + (num%4),rem-1)

cnt = 0
for i in range(1,100):
    for j in range(2,6):
        if F(i,j) != 0 :
            cnt+=1
            break
print(cnt) # 34
