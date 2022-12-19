with open('input.txt') as f:
    input = f.read()

def findPos():
    #Uncomment for Part 1
    #p = 3
    #Uncomment for Part 2
    p=13
    
    
    i = 0
    while(i<len(input)):
        str = input[i:i+1+p]
        for ch in str:
            if(str.count(ch)>1):
                break
            elif(str[p] == ch):
                return i+1+p
        i+=1

print(findPos())