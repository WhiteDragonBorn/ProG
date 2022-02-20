# 16 --- 3695 --- KP
def F(n):
    if n <= 5 :
        return n
    if n > 5 and n%3==0 and F(n/3+2) is not None:
        return n + F(n/3+2)
cnt = 0

for x in range(0,10000):
    if F(x) is not None and F(x)>1000:
        cnt = x
        break
print(cnt)












