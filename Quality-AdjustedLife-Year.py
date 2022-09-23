t = int(input())
sum = 0
while t:
    mul = 1
    a, b = input().split()
    mul = float(a) * float(b)
    sum += mul
    t -= 1
print(sum)
