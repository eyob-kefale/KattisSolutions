import math
x,y,z=map(int,input().split())
a=y//z
x=x-1

b=x//a
print(math.ceil(x/a))
  