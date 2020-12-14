a = int(input("a="))
b = int(input("b="))

res = 1
if b<0:
  for i in range(1,-1*b+1): 
      res *= 1/a
elif a==0 and b==0:
  res = "Cannot calculate!!!"
else:
  for i in range(1,b+1):
      res = res*a 

print("a^b:",res)