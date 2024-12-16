f=open('input9.txt').read()

g=[]
d=[]
id=0

for i in range(len(f)):         #g is for pt1, d is for pt2. g format is as seen in example on page. d format is [ID, blocks], [-1 (blank), blocks], etc.
    if i%2 == 0:                #even index is file
        d.append([id,int(f[i])])
        for j in range(int(f[i])):
            g.append(id)
        id+=1
    else:                       #odd is blank space
        for j in range(int(f[i])):
            g.append(-1)
        d.append([-1,int(f[i])])

i=0
while i <len(g):        #if blank space, move last item in list over
    if g[i]==-1:
        g[i]=g.pop(len(g)-1)
    else:
        i+=1

pt1=0
for i in range(len(g)):
    pt1+=(i*g[i])
print(pt1)

def consolidate(d):         #combine consecutive blank space blocks
    i=0
    while i<len(d)-1:
        if d[i][0]==-1 and d[i+1][0]==-1:
            d[i][1]+=d[i+1][1]
            d.pop(i+1)
        else:
            i+=1
    return d

id-=1           #was previously at 1 above max id

while id>0:            #start at max id and count down
    found=False
    for j in reversed(range(len(d))):    #start from end of list to find ID block
        if found:                        #if it's found then this loop wil break and run consolidate for adjacent empty spaces (ex. [[-1,3], [-1,1]] becomes [-1,4]
            d=consolidate(d)
            break
        if d[j][0]==id:                #find id
            found=True
            lengthfound=d[j][1]        #storing length of file ID as indecies will start moving around
            for i in range(j):            #loop to search for empty space
                if d[i][0]==-1 and d[i][1]>=lengthfound:            #valid empty space found
                    spacefound=d[i][1]        #store length of empty space
                    d[j]=[-1, lengthfound]        #replace file we are moving with empty space
                    d.pop(i)            #remove valid empty space block
                    d.insert(i,[id,lengthfound])        #insert file into new spot
                    if spacefound>lengthfound:        #if there was excess empty space, add it to after the newly moved file
                        d.insert(i+1,[-1,spacefound-lengthfound])
                    break
    id-=1        #look for next ID

g=[]

for i in d:             #convert part 2 to part 1 fmt
    for j in range(i[1]):
        g.append(i[0])

pt2=0

for i in range(len(g)):     #score calc
    if g[i]!=-1:
        pt2+=(i*g[i])
print(pt2)
