test=int(input())
for i in range(test):
    n,m,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    new=[]
    v=n+m
    number=0
    idx1=0
    idx2=0

    while number<v:
        number+=1
        if idx1<n and idx2<m:
            if arr1[idx1]<=arr2[idx2]:
                new.append(arr1[idx1])
                idx1+=1
            else:
                new.append(arr2[idx2])
                idx2+=1
        else:
            if idx1<n:
                new.append(arr1[idx1])
                idx1+=1
            else:
                new.append(arr2[idx2])
                idx2+=1
    
    print(new[k-1]) 