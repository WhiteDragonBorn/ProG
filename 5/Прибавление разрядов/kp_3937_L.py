# 5 --- 3937 --- KP
for N in range(1,10000):
    N_bin = bin(N)[2:]
    summa = 0
    
    for x in N_bin:
        summa+=int(x)
        
    N_bin += str(summa%2)
    
    if N_bin.count('1') > N_bin.count("0"):
        N_bin += "0"
    else:
        N_bin+= "1"
        
    if int(N_bin,2)>80:
        print(int(N_bin,2))
        break
