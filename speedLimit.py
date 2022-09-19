while 1:
    t = int(input())
    d = {}
    l = []
    if t == -1:
        break
    ans = 0
    for i in range(t):
        a, b = map(int, input().split())
        d[b] = a
        l.append(b)
    for x in range(0, len(l)):
        if x == 0:
            ans += l[x] * d[l[x]]
        else:
            ans += (l[x] - l[x - 1]) * d[l[x]]
    print(f"{ans} miles")
