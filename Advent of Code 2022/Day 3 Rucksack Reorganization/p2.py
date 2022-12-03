with open('input.txt') as f:
    input = f.readlines()
    
def priority(ch):
    if (ord(ch) > 96):
        num =  (ord(ch) - 97) + 1
    else:
        num =  (ord(ch) - 65) + 27
    return num

temp = ""
count = 0
i = 0
con = 0
index = int(len(input))
while(i<index):
    for ch in input[i].replace("\n",""):
        if(ch in input[i+1].replace("\n","") and ch in input[i+2].replace("\n","")):
            print(ch)
            con += priority(ch)
            break
    i += 3
print(con)

