# 24 --- 149 --- KP
lat = {}

with open("C:/Users/derde/Desktop/24-s2.txt","r") as f:
    
    bef = f.read(1)
    now = f.read(1)
    then = f.read(1)

    while True:
        if then == "":
            break
        if now not in lat:
            lat[now] = 0
        if bef == 'X' and then == 'Z':
            lat[now] +=1
        bef = now
        now = then
        then = f.read(1)

print (lat)# X ,73