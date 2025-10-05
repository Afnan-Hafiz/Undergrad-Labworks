## 10 23241004 CSE-09E-21L-39 23241004
test=int(input())
for i in range(test):
    n,m=map(int, input().split())
    u=list(map(int, input().split()))
    v=list(map(int, input().split()))
    w=list(map(int, input().split()))
    li={}
    for i in range(n+1):
        li[i]=[]
    for i in range(m):
       li[u[i]].append((v[i],w[i]))
    for i in range(1,n+1):
        print(i, end=": ")
        if m!=0:
            for val in li[i]:
                print(f"({val[0]},{val[1]})", end=" ")
            print()
        else:
            print()

