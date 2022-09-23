W = int(input())
t = int(input())
a = []
while t > 0:
    m = list(map(int, input().split()))
    a.append(m[0] * m[1])
    t -= 1
sum = 0
for x in a:
    sum += x

print(int(sum / W))
