a = list(map(str, input()))

s = set()
for x in range(len(a) + 1):
    if x >= len(a):
        break
    if a[x] == ":" or ";":
        x += 1
        if x >= len(a):
            break
        elif a[x] == "-":
            if a[x + 1] == ")":
                s.add(x - 1)
                x += 1
            else:
                x += 0
        elif a[x] == ")" and a[x - 1] != "-" and a[x - 1] == ":":
            s.add(x - 1)
            x += 1
s = sorted(s)
for x in s:
    print(x)
