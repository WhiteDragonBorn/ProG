def F(num,a):
    if a == 0:
        if num == 80:
            return 1
        return 0
    return F(num+1,a-1) + F(num*2,a-1) + F(num + num%4,a-1)
cnt = 0
for num in range (1000):
    if F(num,5) != 0:
        cnt +=1 
print (cnt)