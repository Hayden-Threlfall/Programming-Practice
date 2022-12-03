with open('input.txt') as f:
    input = f.readlines()
    #    ROCK           PAPER         Scicors
rps = {"A":1,"X":1, "B":2, "Y":2, "C":3, "Z":3}
temp = 0
p1 = 0
p2 = 0
for str in input:
    temp = str.replace("\n","").rsplit(" ")
    
###Part 1###
#    p1 += rps[temp[0]]
#    p2 += rps[temp[1]]
#    if (rps[temp[0]] == rps[temp[1]]):
#        p1 += 3
#        p2 += 3
#    elif(rps[temp[0]] == 1 and rps[temp[1]] == 3):
#        p1 += 6
#    elif(rps[temp[0]] == 2 and rps[temp[1]] == 1):
#        p1 += 6
#    elif(rps[temp[0]] == 3 and rps[temp[1]] == 2):
#        p1 += 6
#    else:
#        print(temp)
#        p2 += 6
###Part 2###
    p1 += rps[temp[0]]
    if(rps[temp[1]] == 1): #lose
        p1 += 6
        p2 += ((((rps[temp[0]]) + 1 )%3) + 1)
    elif(rps[temp[1]] == 2): #draw
        p1 += 3
        p2 += (rps[temp[0]]) + 3
    elif(rps[temp[1]] == 3): #win
        p2 += ((rps[temp[0]]%3) + 1) + 6
    else:
        print("FAIL")
print((p2))
