a = input("Enter number 1: ")
b = input("Enter number 2: ")

if len(a)<=len(b):
    count = 0
    for i in range(1,len(a)+1):
        if a[-1*i]==b[-1*i]:
            count +=1
    print(count)

else:
    count = 0
    for i in range(1,len(b)+1):
        if a[-1*i]==b[-1*i]:
            count +=1
    print(count)