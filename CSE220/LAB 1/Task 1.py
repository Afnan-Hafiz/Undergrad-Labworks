def mergeSortedArray(arr1, arr2):
  v=len(arr1)+len(arr2)
  arr3=np.zeros(v, dtype=int)
  i=0
  j=0
  k=0

  while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
      arr3[k]=arr1[i]
      i+=1
    else:
      arr3[k]=arr2[j]
      j+=1
    k+=1

  while i<len(arr1) or j<len(arr2):
    if i<len(arr1):
      arr3[k]=arr1[i]
      i+=1
      k+=1
    else:
      arr3[k]=arr2[j]
      j+=1
      k+=1

  return arr3

#DRIVER CODE
a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))