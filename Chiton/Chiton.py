count = 0
posx = 0
posy = 0

with open('input-small.txt') as f:
    input = f.readlines()
rows = len(input)
cols = len(input[0])
arr = [0 for j in range(rows)]
for i in range(rows):
    arr[i] = input[i].replace("\n","")

while(posy != rows-1 & posx != cols-1):
    for m in range(4):
        
        if(posx > 0 & posx > 0 & posx != "#" & posx != "#" ):
            print()
        

print(bool())

for i in range(rows):
    print(arr[i])