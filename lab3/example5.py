n = int(input("Enter the number: "))
res = 1
if n<0:
  res = "Cannot calculate!!!"
for i in range(2,n+1):
    res = res*i
print(str(n)+"! =",res)
