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
for str in input:
    temp = [str[:int(len(str)/2)], str[int(len(str)/2):].replace("\n","")]
    for ch in temp[0]:
        if (temp[1].find(ch) >= 0):
            count += priority(ch)
            break
print(count)

