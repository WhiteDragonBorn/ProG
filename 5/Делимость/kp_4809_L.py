# 5 --- 4809 --- KP
for N in range(1,100000):
    R = str(N)
    S_1 = 0
    S_2 = 0
    
    cnt = 1
    for x in R:
        if int(x)%2 == 0:
            S_1+=int(x)
            
        if cnt%2!=0:
            S_2+=int(x)
        cnt+=1
        
    RE = abs(S_1-S_2)
    
    if RE == 27:
        print(N) #90909
   
