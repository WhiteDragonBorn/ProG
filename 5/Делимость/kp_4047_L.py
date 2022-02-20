# 5 --- 4047 --- KP
for N in range(1,100000):
    R = N
    if R%3==0:
        R /= 3
    else:
        R -=1
    if R%5==0:
        R /= 5
    else:
        R -=1
    if R%11==0:
        R /= 11
    else:
        R -=1
    if R == 8:
        print(N) # 4
