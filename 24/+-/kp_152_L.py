# 24 --- 152 --- KP
A = open(r'C:\Users\MYC\Desktop\ege2022kp\24data\24-j9.txt','r')
s = A.readline()
k = len(s)
d = k//2
cnt = 0
for i in range(d):
    if s[i] == s[(k-1)-i]:
        cnt+=1
print(cnt) # 19351
