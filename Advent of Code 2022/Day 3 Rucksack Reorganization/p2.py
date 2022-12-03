with open('input-small.txt') as f:
    input = f.readlines()
    
def priority(ch):
    if (ord(ch) > 96):
        num =  (ord(ch) - 97) + 1
        print()
    else:
        num =  (ord(ch) - 65) + 27
    return num

temp = 0
count = 0

str = input[0].replace("\n","")
for ch in str:
    
    print()



count = 1
for ch in str:
    #print(ch)
    for i in range(len(input)-1):
        input[i+1]
        if(input[i+1].find(ch) >= 0):
            count += 1
            i += 1
    if(count == 3):
        break
print(ch)

