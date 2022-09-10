import math

N, K = input().split(" ")
m = list(map(int, input().split(" ")))
n = int(N)
k = int(K)
x = math.floor(n / k)

for i in range(k - 1, n, k):
    print(m[i], end=" ")