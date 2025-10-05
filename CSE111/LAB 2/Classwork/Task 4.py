def show_palindrome(n):
  for i in range(1,len(n)+1,1):
    print(i,end="")
  for i in range(len(n)-1,0,-1):
    print(i,end="")
n=input()
show_palindrome(n)