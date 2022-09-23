n = list(map(int, input().split()))
b = n[1]

l = []
while n[1] > 0:

    a = input()
    l.append(int(a))
    n[1] -= 1
sum = 0
if n[0] == b:
    for i in l:
        sum += i
    print(sum / n[0], "", sum / n[0])
else:
    dif = n[0] - b
    min = -1 * (dif * 3)
    max = dif * 3
    for i in l:
        sum += i
    tmin = min + sum
    tmax = max + sum
    print((tmin / n[0]), "", (tmax / n[0]))
