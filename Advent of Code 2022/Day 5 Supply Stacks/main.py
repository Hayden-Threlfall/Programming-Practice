with open('input.txt') as f:
    input = f.readlines()
pos = []
moves = []
arr = [[]]


def split():
    spl = 0
    for str in input:
        if (str == "\n"):
            break
        else:
            spl+=1
    return([input[:spl],input[spl+1:]])

#Make Arrays
temp = split()
pos = temp[0]
moves = temp[1]
i=0
ch = ""
str = pos[int(len(pos))-1].replace("\n","")
for ch in str:
    if(ch.isdigit()):
        if(i>0):
            arr.append([])
        i+=1
i=0
for str in pos:
    for ch in str:
        if(ch.isalpha()):
            arr[int((i-1)/4)].insert(0,ch)
        i+=1
    i = 0

#PART 1
"""
for line in moves:
    line = line.replace("\n", "").split(" ")
    for i in range(0, int(line[1])):
        
for i in arr:
   print(i[len(i)-1])
"""

#Part 2
i = 0
for line in moves:
    line = line.replace("\n", "").split(" ")
    arr[int(line[5])-1]+=(arr[int(line[3])-1][-int(line[1]):])
    arr[int(line[3])-1][-int(line[1]):] = []
for i in arr:
   print(i[len(i)-1])