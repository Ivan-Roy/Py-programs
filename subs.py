"""
Method 1: taking substring input from user
"""
s1=input("Enter any string ")
b=[]
while 1:
  s2=input("Enter any substring ")
  if(s2 in s1):
    b.append(s2)
  if(len(s2)>len(s1)):
    print("substring length cannot be greater than original string!! ")
    break
  if(s2 not in s1):
    continue
print("Substrings present are : ")
for i in b:
  print(i,end=" ")
