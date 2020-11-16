n = int(input("Enter the number: "))
res = 1
if n<0:
  res = "Cannot calculate!!!"
for i in range(2,n+1):
    res = res*i
print(str(n)+"! =",res)

value = list(str(res))
trailing_zeros = 0
value.reverse()
for i in range(len(value)):
  if value[i] == "0":
    trailing_zeros +=1
  else:
    break
print(str(n) + " factorial" + " has " + str(trailing_zeros) + " trailing_zeros")
