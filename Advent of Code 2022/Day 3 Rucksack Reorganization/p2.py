with open('input.txt') as f:
    input = f.readlines()
    
def priority(ch):
    if (ord(ch) > 96):
        num =  (ord(ch) - 97) + 1
    else:
        num =  (ord(ch) - 65) + 27
    return num

temp = 0
count = 0
str = input[0].replace("\n","")
count = 0
end = True
i = 0
con = 0
index = int(len(input))
index = 12
while(i<index):
    for ch in input[i].replace("\n",""):
        for j in range(3):
            temp = input[i+j].replace("\n","")
            #print((i+j))
            if(temp.find(ch) >= 0):
                count += 1
        if(count == 3):
            break
        count = 0
    i += 3
    print(ch)
    con += priority(ch)
print(con)

