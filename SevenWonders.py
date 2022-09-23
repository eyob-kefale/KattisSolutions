import math


A = [str(x) for x in input()]
T = int(0)
C = int(0)
G = int(0)
a = int(0)
for c in range(len(A)):
    if A[c] == "T":
        T += 1
    elif A[c] == "C":
        C += 1
    elif A[c] == "G":
        G += 1
min = min(T, (min(C, G)))
a = 7 * min
a = (T**2) + (C**2) + (G**2) + a
print(a)