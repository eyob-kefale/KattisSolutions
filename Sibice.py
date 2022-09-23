from math import sqrt
t = list(map(int, input().split()))
while t[0] > 0:
    a = int(input())
    q = sqrt((t[1] ** 2) + (t[2] ** 2))

    if q >= a:
        print("DA")
    else:
        print("NE")
    t[0] -= 1
