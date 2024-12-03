g=open("input3.txt").read()

pt1=0
pt2=0

on=True

for i in range(len(g)):
    if g[i:].startswith("do()"):
        on=True
    if g[i:].startswith("don't()"):
        on=False
    if g[i:].startswith("mul("):
        mul=g[i:i+12]
        value = mul.split("mul(")[1].split(")")[0]
        try:
            a, b = value.split(",")
            if a.isdigit() and b.isdigit():
                pt1 += int(a) * int(b)
                if on: pt2 += int(a) * int(b)
        except ValueError:
            pass

print("Part 1:", pt1, "Part 2:", pt2)
