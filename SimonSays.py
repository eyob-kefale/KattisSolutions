t = int(input())
while t:
    s = list(map(str, input().split()))
    if s[0] == "Simon" and s[1] == "says":
        s.remove(s[0])
        s.remove(s[0])
        print(*s)
    t -= 1