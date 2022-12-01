with open('input.txt') as f:
    input = f.readlines()
cal = list()
cal.append(0)
temp = 0
for val in input:
    if(val != "\n"):
        temp = int(val.replace("\n",""))
        cal[len(cal)-1] += temp
    else:
        cal.append(0)
cal.sort()
temp = 0
for i in range(3):
    temp += cal[len(cal)-1-i]
    print(temp)
print(temp)
