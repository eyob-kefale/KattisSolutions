t = int(input())
d = {}
for i in range(t):
    a, b = map(int, input().split())
    d[a] = b
l = []
s = []
for x in d:
    l.append(x)
for x in range(1, len(l)):
    ava = (d[l[x]] - d[l[x - 1]]) // (l[x] - l[x - 1])
    s.append(ava)
s.sort(reverse=True)
print(s[0])
