f=open("input3.txt").read()
g=str(f)

pt1=0
pt2=0

print("f".find("mul("))

values = [part.split(")")[0] for part in f.split("mul(")[1:]]

f=f.split("mul(")

for value in values:
    try:
        a,b=value.split(",")
        if a.isdigit() and b.isdigit():
            pt1+=int(a)*int(b)
    except ValueError:
        pass

print(pt1)

on=True

for i in range(len(g)):
    if g[i:].startswith("do()"):
        on=True
    elif g[i:].startswith("don't()"):
        on=False
    elif g[i:].startswith("mul(") and on:
        mul=g[i:i+12]
        value = mul.split("mul(")[1].split(")")[0]
        try:
            a, b = value.split(",")
            if a.isdigit() and b.isdigit():
                pt2 += int(a) * int(b)
        except ValueError:
            pass

print(pt2)
