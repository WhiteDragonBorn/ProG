# 5 --- 3421 --- RE

def ONE(num):
    NN = int(num,2) >> 1 # Сдвиг вправо на 1 0b0101 -> 0b0010
    NN = bin(NN)[2:]
    
    for j in range(8-len(NN)): # Делаем 8 бит опять
        NN = "0"+NN
        
    return NN

def TWO(num):
    NN = int(num,2) + 4
    NN = bin(NN)[2:]
    
    for j in range(8-len(NN)): # Делаем 8 бит опять
        NN = "0"+NN
        
    return NN

for i in range(191,192): # Сделал перебор с задеЛом на будущее
    N = bin(i)[2:]
    
    for j in range(8-len(N)): 
        N = "0"+N
##    print(int(N,2),int(ONE(N),2),int(TWO(N),2)) # Дебаг
    print( int( TWO(ONE(ONE(TWO(ONE(ONE(N)))))),2) ) # 16, именно это задание легче ручками решать!
    
    
    
        
