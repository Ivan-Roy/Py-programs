n=int(input("Enter any number "))
def factor(n):
  for i in range(1,n+1):
    if(n%i==0):
      print(i)
a=factor(n)
