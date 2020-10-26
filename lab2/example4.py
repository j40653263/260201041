age = int(input("How old are you?: "))
fee = 3
if age<6 or age>60:
    print("Free!")
elif age<=18:
    d_fee = fee - fee*0.5
    print("Ticket fee: ",d_fee,"TL")
else:
    print("Ticket fee: ",fee,"TL")
