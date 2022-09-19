t = int(input())
cnt = 0
while t:
    cnt += 1
    a, b = input().split()
    b = int(b)
    sum = int(b * (b + 1) / 2)
    osum = int(b * b)
    esum = int(b * (b + 1))
    print(cnt, sum, "", osum, "", esum)
    t -= 1
