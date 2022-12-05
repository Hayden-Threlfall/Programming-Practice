with open('input-small.txt') as f:
    input = f.readlines()
temp = 0
Tlis = list()
lis = list()
def split(str):
    temp = str.replace("\n","").rsplit("-")
    Tlis.append(temp[0])
    Tlis.append(temp[1].rsplit(",")[0])
    Tlis.append(temp[1].rsplit(",")[1])
    Tlis.append(temp[2])
    for i in Tlis:
        print()

    return(Tlis)

for str in input:
    print(split(str))