def mostWater(arr):
 count=0
 for i in range (len(arr)):
    for j in range(i+1,len(arr)):
      width= j-i
      if arr[i] <arr[j]:
        area= arr[i]*width
      else:
        area=width*arr[j]

      if count<area:
        count=area
 return count


#driver
height = np.array([1,8,6,2,5,4,8,3,7])
print(f'Given Array: {height}')

print(f'\nExpected Output: 49')
print(f'Your Output: ',end='')
mostWater(height)
