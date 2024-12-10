f=open("input6.txt").read()

f=[i for i in f.split("\n")]

pt1=0

pos=[]
defaultPos=[]
dir=[-1,0]
defaultDir=[-1,0]
steps=0
passed=set()

def step(input,dir,pos):
    x=pos[0]+dir[0]
    y=pos[1]+dir[1]
    if input[x][y]=='#':
        if dir[0]==-1:              #up
            return pos, [0,1], True, [x,y]
        elif dir[0]==1:               #down
            return pos, [0,-1], True, [x,y]
        elif dir[1]==-1:          #right
            return pos, [-1,0], True, [x,y]
        elif dir[1]==1:               #left
            return pos, [1,0], True, [x,y]
    return [x,y], dir, False, [x,y]

def isloop(input, pos, dir):
    steps=set()
    # print(input)
    while pos[0] >= 0 and pos[0] < len(input) - 1 and pos[1] >= 0 and pos[1] < len(input[0]) - 1:
        pos, dir, turned, block = step(input, dir, pos)
        # print(steps, pos, dir)
        if tuple(pos+dir) not in steps:
            steps.add(tuple(pos+dir))
        elif tuple(pos+dir) in steps:
            # print("returned true")
            return True
    # print("returned false")
    return False

for i in range(len(f)):
    for j in range(len(f)):
        if f[i][j]=="^":
            pos=[i,j]

defaultPos=list(pos)

print(len(f), len(f[0]), pos)
passed.add(tuple(pos))

while pos[0]>=0 and pos[0]<len(f)-1 and pos[1]>=0 and pos[1]<len(f[0])-1:
    pos,dir, _, _= step(f,dir,pos)
    passed.add(tuple(pos))

print("part1:", len(passed))

inputs=[]
for i in range(len(f)):
    for j in range(len(f[i])):
        if [i,j] != defaultPos:
            tmpIn=list(f)
            tmpIn[i]=tmpIn[i][:j]+"#"+tmpIn[i][j+1:]
            inputs.append(tmpIn)

pt2=0

for input in inputs:
    # print(input, defaultPos, defaultDir)
    if isloop(input, defaultPos, defaultDir):
        pt2+=1

print(pt2)
