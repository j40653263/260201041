a = input("Enter number 1: ")
b = input("Enter number 2: ")

if len(a)<=len(b):
    count = 0
    for i in range(1,len(a)+1):
        if a[-1*i]==b[-1*i]:
            count +=1

else:
    count = 0
    for i in range(1,len(b)+1):
        if a[-1*i]==b[-1*i]:
            count +=1

print(count)

"""
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 1: "))
c = 0
while True:
  if n1 %10 == n2%10:
    c += 1
  n1 //= 10
  n2 //= 10
  if n1==0 and n2==0:
    break

print(c)  
"""
