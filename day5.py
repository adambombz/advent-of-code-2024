from collections import defaultdict

f=open('input5.txt').read().split("\n\n")

order = defaultdict(list)
revorder = defaultdict(list)
out,bad=[],[]
pt1,pt2=0,0

for i in f[0].split("\n"):
    x,y = i.split("|")
    order[x].append(y)
    revorder[y].append(x)

updates=[x.split(",") for x in f[1].split("\n")]

for update in updates:
    s=True
    for i in range(len(update)):
        orders=order[update[i]]
        revorders=revorder[update[i]]

        if i!=(len(update)-1):
            for o in update[i+1:]:
                if o not in orders:
                    s=False

        if i!=0:
            for o in update[:i]:
                if o not in revorders:
                    s=False

    if s:
        out.append(update)
    else:
        bad.append(update)

for i in out:
    pt1+=int(i[int(len(i)/2-0.5)])

print("part 1:",pt1)

out=[]

def correct(x,y,order):
    if y in order[x]:
        return True
    else:
        return False

for i in bad:
    for n in range(len(i) - 1, 0, -1):
        swapped = False
        for j in range(n):
            if correct(i[j+1],  i[j],order):
                i[j], i[j + 1] = i[j + 1], i[j]
                swapped = True
        if not swapped:
            break
    out.append(i)

for i in out:
    pt2+=int(i[int(len(i)/2-0.5)])

print("part 2:",pt2)
