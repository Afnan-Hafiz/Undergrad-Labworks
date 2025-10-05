def mergeSort(arr):
  if len(arr) <= 1:
    return arr, 0

  mid= len(arr)//2
  left, leftcount = mergeSort(arr[:mid])
  right, rightcount = mergeSort(arr[mid:])
  rightSquared = sorted([x*x for x in right])
  count= leftcount + rightcount
  j=0
  for i in range(len(left)):
    while j<len(rightSquared) and left[i]>rightSquared[j]:
      j += 1
    count += j

  merge =[]
  i=0
  j=0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merge.append(left[i])
      i += 1
    else:
      merge.append(right[j])
      j += 1

  while i < len(left):
    merge.append(left[i])
    i+=1
  while j < len(right):
    merge.append(right[j])
    j += 1

  return merge, count

n = int(input())
arr = list(map(int, input().split()))
listed, result = mergeSort(arr)
print(result)