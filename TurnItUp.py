n = int(input())
a = []
l = 7
for i in range(n):
    b = input()
    a.append(b)
for i in range(n):
    if (a[i] == "Skru op!") and (l < 10):
        l += 1
    elif (a[i] == "Skru ned!") and (l > 0):
        l -= 1
    else:
        if l == 10:
            l = 10
        else:
            l = 0
print(l)
