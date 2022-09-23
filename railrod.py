x = list(map(int, input().split(" ")))
y = (4 * x[0]) + (3 * x[1])
if y % 2 == 0:
    print("possible")
else:
    print("impossible")
