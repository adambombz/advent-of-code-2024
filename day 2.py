f=open("input2.txt").read().split("\n")

levels=[]
pt1bad=0
pt2bad=0

for i in f:                         #build input into levels
    level=[]
    for j in i.split(" "):
        level.append(int(j))
    levels.append(level)

def checkLevel(level):
    if level[0]>level[1]:           #decreasing first two numbers
        for j in range(len(level)-1):
            if (level[j]-level[j+1])>3 or (level[j]-level[j+1])<=0:     #difference is too big or going in wrong direction fails function
                return False
    elif level[0]<level[1]:         #increasing first two numbers
        for j in range(len(level)-1):
            if (level[j]-level[j+1])<-3 or (level[j]-level[j+1])>=0:    #difference is too big or going in wrong direction
                return False
    else:                           #same first number
        return False

    return True                     #level is valid

for level in levels:
    if not checkLevel(level):
        pt1bad+=1
        newLevels=[]
        newResults=[]
        for j in range(len(level)):         #build new levels with removing one of the digits
            tempLevel=level.copy()
            tempLevel.pop(j)
            newLevels.append(tempLevel)
        for newLevel in newLevels:          #check all new levels
            newResults.append(checkLevel(newLevel))
        if True not in newResults:          #if one of new levels doesn't work then level fails pt2
            pt2bad+=1

print("Part 1:", len(levels)-pt1bad)        #subtract bad from all to get good
print("Part 2:", len(levels)-pt2bad)
