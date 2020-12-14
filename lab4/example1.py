num = int(input("Enter an integer: "))
ones = num%10
tens = (num%100) // 10
print("Sum of the last two digit is,",ones+tens)
