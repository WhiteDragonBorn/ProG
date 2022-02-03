# 17 --- 37337 --- RE
f = open(r'D:\Downloads\17.txt','r')
mas = []
while True:
    num = f.readline()
    if num == '':
        break
    mas.append(int(num))
cnt = 0
maxsum = 0
for i in range(0,len(mas)):
    for j in range(i+1,len(mas)):
        PER = mas[i] ; VTO = mas[j]
        if( (PER % 160 != VTO % 160) and (PER%7==0 or VTO%7==0) ):
            cnt+=1
            maxsum = max(maxsum,PER+VTO)
print(cnt,maxsum) # 12749665 19989
