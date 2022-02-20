# 5 --- 4930 --- KP
for N in range(1,100000):
    R = bin(N)[2:]
    if N%2 == 0:
        summa = 0
        for x in R:
            summa += int(x)
        summa = bin(summa)[2:]
        R += summa
    else:
        R = "1" + R + "00"
    if int(R,2) > 215:
        print(N) # 23
        break
    
