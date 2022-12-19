with open('input-small.txt') as f:
    input = f.readlines()
arr = []
i = -1
for str in input:
    temp = str.replace("\n","").rsplit(" ")
    if(str.count("$ cd ")>0):
        arr.append([])
        i +=1
        arr[i].append(temp[2])
        
    if(temp[0].isdigit()):
        arr[i].append(int(temp[0]))
print(arr)

#Find size less than 100000
count = 0
fCount=0
for i in arr:
    for j in range(1, len(i)):
        count += i[j]
        
        
#####The problem with this code is I count the files i the directory, I need to count the other directories that come after too.


if(count<=100000):
        fCount += count
    count = 0
    
        
print(fCount)