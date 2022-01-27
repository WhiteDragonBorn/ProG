# 5 --- 3421 --- REz
def move(num):
    num = list(bin(num)[2:])
    rn = len(num)-1
    while rn >=0:
        if rn == 0:
            num[rn] = "0"
            break
        num[rn] = num[rn-1]
        rn = rn-1
    num = int("".join(num),2)
    return num
        
num = 191
num = move(move(num))
num +=4
num = move(move(num))
num +=4
print(num)#16