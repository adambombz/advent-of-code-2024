f=open('input4.txt').read().splitlines()

input=[]
pt1,pt2=0,0

for i in f:
    input.append(list(i))

def xmas(x,y,c,cord):
    total=0
    for i,j in cord:
        # print(i,j)
        if i>=0 and i<len(input) and j>=0 and j<len(input[i]) and input[i][j]==c:
            if i>x and j>y:
                cord=[[i+1,j+1]]
            elif i==x and j>y:
                cord=[[i,j+1]]
            elif i<x and j>y:
                cord=[[i-1,j+1]]
            elif i<x and j==y:
                cord=[[i-1,j]]
            elif i<x and j<y:
                cord=[[i-1,j-1]]
            elif i==x and j<y:
                cord=[[i,j-1]]
            elif i>x and j<y:
                cord=[[i+1,j-1]]
            elif i>x and j==y:
                cord=[[i+1,j]]
            if c=='M':
                # print('found M at', i, j)
                total+=xmas(i,j,'A',cord)
            elif c=='A':
                # print('found A at', i, j,)
                total+=xmas(i,j,'S',cord)
            elif c=='S':
                # print('found S at', i, j)
                total+=1
    return total

for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y]=='X':
            # print("found X at",x,y)
            cord=[]
            for i in [x-1,x,x+1]:
                for j in [y-1,y,y+1]:
                    cord.append([i,j])
            # print(cord)
            pt1+=xmas(x,y,'M',cord)

print(pt1)

for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y] == 'A' and x-1>=0 and x+1<len(input) and y-1>=0 and y+1<len(input[x]) and ((input[x+1][y+1]=='S' and input[x+1][y-1]=='M' and input[x-1][y-1]=='M' and input[x-1][y+1]=='S') or (input[x+1][y+1]=='S' and input[x+1][y-1]=='S' and input[x-1][y-1]=='M' and input[x-1][y+1]=='M') or (input[x+1][y+1]=='M' and input[x+1][y-1]=='S' and input[x-1][y-1]=='S' and input[x-1][y+1]=='M') or (input[x+1][y+1]=='M' and input[x+1][y-1]=='M' and input[x-1][y-1]=='S' and input[x-1][y+1]=='S')):
            pt2+=1
print(pt2)
