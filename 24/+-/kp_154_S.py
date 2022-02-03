#24 --- 154 --- kp

mn = 0
cnt = 0
flag = False
with open("C:/Users/derde/Desktop/24-153.txt","r") as F:
    sym = F.read(1)
    while sym != "":
        if sym == "D" and not flag: 
            cnt += 1 
            flag = True
        elif sym != "D" and flag:
            cnt += 1 
        elif sym == "D" and flag:
            cnt += 1 
            if mn == 0 and cnt > 2: 
                mn = cnt
            if cnt > 2 and mn > cnt:
                mn = cnt 
            cnt = 1
        sym = F.read(1)
print(mn)#139