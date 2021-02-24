s1=input("Enter string 1 ")
s2=input("Enter string 2 ")
a,b=0,0
for i in s1:
  if (i != " "):
    a+=1
for i in s2:
  if (i !=" "):
    b+=1
    
print(a)
print(b)
g=0
s3=s1.split()
s4=s2.split()
x=list(s3)
y=list(s4)
a,b=0,0
for i in x:
  if i in y:
    a+=1
  else:
    continue
print(a)
for i in s1:
  if i in s2:
    b+=1
print(b)    
