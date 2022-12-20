with open('input.txt') as f:
    input = f.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n","")
seen = 0
seen += len(input)*2
seen += (len(input[0])*2)-4

temp = 0
lenj = len(input[0])
for i in range(1, len(input)-1):
    temp = input[i][0]
    for j in range(1, lenj):
        if(int(temp) < int(input[i][j])):
            seen+=1
            temp=int(input[i][j])
        else:
            break
for i in range(1, len(input)-1):
    temp = input[i][0]
    for j in range(1, lenj):
        if(int(temp) < int(input[i][lenj-j])):
            seen+=1
            temp=int(input[i][lenj-j])
        else:
            break
for i in range(1, lenj):
    temp = input[i][0]
    for j in range(1, len(input)-1):
        if(int(temp) < int(input[i][j])):
            seen+=1
            temp=int(input[i][j])
        else:
            break
for i in range(1, lenj):
    temp = input[i][0]
    for j in range(1, len(input)-1):
        if(int(temp) < int(input[i][lenj-j])):
            seen+=1
            temp=int(input[i][lenj-j])
        else:
            break
print(seen)