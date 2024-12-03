from collections import defaultdict

f=open("input1.txt",'r').read().split('\n')

left, right = [],[]
count = defaultdict(int)

pt1=0
pt2=0

for i in f:
    left.append(int(i[:5]))
    right.append(int(i[-5:]))

left.sort()
right.sort()

for i in range(len(left)):
    pt1+=(abs(left[i]-right[i]))
    print(i,left[i],right[i],abs(left[i]-right[i]))

for i in range(len(left)):
    for j in range(len(right)):
        if left[i]==right[j]:
            count[left[i]]+=1

for i in count.keys():
    pt2+=i*count[i]

print(pt1, pt2)

