# 24 --- 153 --- kp наговонокодил))
bol = True
flag = False
mn = 0
cnt = 0
with open('C:/Users/derde/Desktop/24-153.txt','r') as F:
    line = F.readline()
    while line !="":
        for i in range (len(line)):
            if line[i] == "D":
                if flag == True:
                    cnt +=1
                else:
                    flag = True
                    cnt = 1
            else:
                if bol and cnt > 0: 
                    mn = cnt
                    bol = False
                if mn > cnt and cnt != 0: 
                    mn = cnt
                    cnt = 0
                flag = False
        line = F.readline()
    print(mn)#5