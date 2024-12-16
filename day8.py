from collections import defaultdict

f=open('input8.txt').read().splitlines()

grid=defaultdict(list)
valid=set()

def validnode(antinodes):
    out=set()
    for node in antinodes:
        if node[0]>=0 and node[0]<len(f) and node[1]>=0 and node[1]<len(f[0]):
            out.add(tuple(node))
    return out

for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j]!='.' and f[i][j]!='#':
            grid[f[i][j]].append([i,j])

for signal in grid.keys():
    nodes=list(grid[signal])
    for _ in range(len(nodes)):
        node=nodes.pop(0)
        for i in range(len(nodes)):
            cnode=nodes[i]
            if node!=cnode:
                dx=node[0]-cnode[0]
                dy=node[1]-cnode[1]
                antinodes=[[node[0]+dx,node[1]+dy],[cnode[0]-dx,cnode[1]-dy]]
                valid=valid.union(validnode(antinodes))
print("pt1",len(valid))

valid=set()

for signal in grid.keys():
    nodes=list(grid[signal])
    for _ in range(len(nodes)):
        node=nodes.pop(0)
        for i in range(len(nodes)):
            cnode=nodes[i]
            if node!=cnode:
                dx=node[0]-cnode[0]
                dy=node[1]-cnode[1]
                antinodes=[]
                for j in range(len(f)):
                    antinodes.append([node[0]+dx*j,node[1]+dy*j])
                    antinodes.append([cnode[0]-dx*j,cnode[1]-dy*j])
                valid=valid.union(validnode(antinodes))
print("pt2",len(valid))
