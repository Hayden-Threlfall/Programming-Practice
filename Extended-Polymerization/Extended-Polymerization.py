import os
from collections import Counter
steps = 40 ##Manually set

cols = 0
rows = 0
keys = list()
values = list()
dic = 0
str = ""
tempS = ""
newStr = list()

os.listdir()
with open('input.txt') as f:
    lines = f.readlines()

str = lines[0].replace("\n","")
rows = len(lines)-2
values = [0 for y in range(rows)]
keys = [0 for y in range(rows)]

for i in range(rows):
    keys[i] = lines[2+i].replace("\n","").rsplit(" -> ")[0]
    values[i] = lines[2+i].replace("\n","").rsplit(" -> ")[1]
dic = dict(zip(keys, values))


for s in range(steps):
    newStr = list()
    newStr.extend(str[0])
    for i in range(len(str)-1):
        tempS = str[i] + str[i+1]
        newStr.extend(dic[tempS])
        newStr.extend(tempS[1])
    str = ("".join(newStr))
##    print(s)

##This is a slower method of the above for loop
#for s in range(steps):
#    newStr = ""
#    newStr = str[0]
#    for i in range(len(str)-1):
#        newStr = newStr + dic[str[i] + str[i+1]] + str[i+1]
#    str = newStr
#    print(s)


counter = Counter(str)
most = counter.most_common()[0]
least = counter.most_common()[-1]
print(most[1]-least[1])


