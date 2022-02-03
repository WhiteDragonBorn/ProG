# 24--- 151 --- kps

cnt = 0
line = []
with open('C:/Users/derde/Desktop/24-j9.txt','r') as F:
    sym = F.read(1)
    for i in range(5):
        line.append(sym)
        sym = F.read(1)
    
    while sym != "":

        
        if line == list(reversed(line)):
            cnt += 1
        for num in range(len(line)-1):
            line[num] = line[num+1]
        sym = F.read(1)
        line[-1] = sym
print(cnt)#1521