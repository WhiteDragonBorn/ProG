# 23 --- P07 --- KP
nlen = 0
mxlen = 0

with open('C:/Users/derde/Desktop/24.txt', 'r') as f:
    ap = f.read(1)


    while True:
        nsym = ap 
        ap = f.read(1)
        if ap == 'X' or ap == 'Y' or ap == 'Z':

            if nsym != ap:
                nlen += 1 
                if nlen > mxlen:
                    mxlen = nlen 
            else:
                nlen = 1
        else: 
            break
    print(mxlen) #35
