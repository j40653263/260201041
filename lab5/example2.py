n = int(input("How many numbers? "))
count = 0
for i in range(n):
    x = int(input("Enter an integer: "))
    if x%2==0:
        count += 1
res = (count/n)*100
print(str(res)+"%")