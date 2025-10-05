## 20 23241004 CSE-09E-21L-41 23241004
import sys
n=int(input())
for i in range(n):
    m=int(input())
    arr=input().split()
    for i in range(m):
        arr[i]=int(arr[i])
    i=0
    u=0
    flag=True

    while flag:
        if i<(m-1):
            if (arr[i]%2==arr[i+1]%2) and (arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                i+=1
                if (i-1>0) and (arr[i-1]< arr[i-2]):
                    u=1
            else:
                i+=1
        else:
            if u==0:
                flag=False
            else:
                flag=True
                i=0
                u=0
    for i in range(m):
        print(arr[i], end=" ")
