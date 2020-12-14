num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

minn = num1

if num2 < num1:
    minn = num2
if num3 < num2:
        minn = num3

print("The minimum number is: ",minn)