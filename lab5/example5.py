a = int(input("How many Fibonacci numbers to generate: "))
x,y = 0,1
for i in range(a):
    print(y,end=" ")
    x,y = y,x+y

print()
"""
b = int(input("How many Fibonacci numbers to generate: "))
x,y = 0,1
count = 0
while count<b:
  print(y,end=" ")
  x,y = y,x+y
  count +=1
"""