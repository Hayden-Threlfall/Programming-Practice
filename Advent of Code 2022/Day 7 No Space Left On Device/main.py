with open('input-small.txt') as f:
    input = f.readlines()
arr = []
i = -1
l = 0
count = 0

for str in input:
    temp = str.replace("\n","").rsplit(" ")
    if(str.count("$ cd ")>0):
        if(temp[2]==".."):
            l-=1
        else:
            arr.append([])
            i +=1
            arr[i].append(l)
            l+=1
        
    if(temp[0].isdigit()):
        arr[i].append(int(temp[0]))
#Find size less than 100000
count = 0
fCount=0
previous = 0
for i in range(len(arr)):
    #Find Dir size
    if(previous > arr[i][0]):
        print("IDK")
    else:
        
        for j in range(1, len(arr[i])):
            count += arr[i][j]
            if(count>100000):
                break
        ###END
        if(count<=100000):
                fCount += count
        count = 0

print(fCount)