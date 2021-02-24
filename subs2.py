"""
Method 2
"""
s1=input("Enter any string ")
b=[]
n=len(s1)
for i in range(0,n):
  for j in range(i,n):
    b.append(s1[i:(j+1)])

print("Substrings are ")
for i in b:
  print(i,end=" ")
