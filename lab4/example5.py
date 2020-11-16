a = int(input("How many Fibonacci numbers to generate: "))
x,y = 0,1
for i in range(a):
    print(y,end=" ")
    x,y = y,x+y