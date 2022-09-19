t=int(input())
while t:
    l=set()
    a,b=map(int,input().split())
    for x in range(a):
        y,z=map(int,input().split())
        if y>0 and z>0:
            l.add(0)
        elif y>0 and z<0:
            l.add(-2)
        elif y<0 and z>0:
            l.add(-1)
        else:
            l.add(1)  
    print(len(l))                  
    
    t-=1