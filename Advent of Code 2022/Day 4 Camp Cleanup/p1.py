with open('input.txt') as f:
    input = f.readlines()

    count = 0


def arrCreate(str):
    str = str.replace("\n","")
    arr = ["","","",""]
    c2 = 0
    c1 = 0
    for i in str:
        if(i.isdigit()):
            arr[c1] += (i)
            c2 +=1
        else:
            c1+=1
            c2 = 0
    return(arr)

for str in input:
    temp = arrCreate(str)
    if((int(temp[2])>=int(temp[0]) and int(temp[3])<=int(temp[1])) or (int(temp[0])>=int(temp[2]) and int(temp[1])<=int(temp[3]))):
        count += 1
print(count)