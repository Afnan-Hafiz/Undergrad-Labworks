## 10 23241004 CSE-09E-21L-41 23241004
a=int(input())
for i in range(a):
    length,sum=map(int, input().split())
    arr=list(map(int, input().split()))
    
    idx1=0
    idx2=length-1
    flag=False
    while idx1<idx2:
        current=arr[idx1]+arr[idx2]
        if current==sum:
            print(idx1+1,idx2+1)
            flag=True
            break
        elif current<sum:
            idx1+=1
        else:
            idx2-=1
    if flag==False:
        print(-1)