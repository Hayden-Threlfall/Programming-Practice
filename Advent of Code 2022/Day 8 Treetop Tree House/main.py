import numpy as np

with open('input-small.txt') as f:
    input = f.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n","")
arr = []
for i in range(len(input)):
    arr.append([])
    for j in range(len(input[0])):
        arr[i].append(int(input[i][j]))
        
seen = 0
seen += len(input)*2
seen += (len(input[0])*2)-4



temp = 0
lenj = len(input[0])-1

bol = [[True]*lenj+1]*lenj+1 ##True or false if this tree has been found
for i in range(lenj):
    bol[0][i] = False
    bol[i][0] = False
    bol[lenj-i][i] = False
    bol[j][lenj-j] = False
print(bol)
        
for i in range(1, lenj):
    temp = input[i][0]
    for j in range(1, lenj):
        if(int(temp) < arr[i][j]):
            seen+=1
            #print(arr[i][j])
            temp=arr[i][j]
        elif(int(temp) <= arr[i][j]):
            seen+=0
        else:
            break
for i in range(1, lenj):
    temp = input[i][0]
    for j in range(1, lenj):
        if(int(temp) < arr[i][lenj-j]):
            seen+=1
            print(arr[i][j])
            temp=arr[i][j]
        elif(int(temp) <= arr[i][lenj-j]):
            seen+=0
        else:
            break    
print(np.matrix(arr))
print(seen)