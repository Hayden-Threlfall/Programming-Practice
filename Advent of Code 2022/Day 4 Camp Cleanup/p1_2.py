with open('input-small.txt') as f:
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
    for l in range(len(arr)):
        arr[l] = int(arr[l])
    return(arr)

for str in input:
    temp = arrCreate(str)
    if(((temp[2])>=temp[0] and temp[3]<=temp[1]) or (temp[0]>=temp[2] and temp[1]<=temp[3])):
        count += 1
print(count)