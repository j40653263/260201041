hasUpper = False
hasLower = False
hasNum = False

pw = input("Please enter a password: ")

for ch in pw:
    if ch>="A" and ch<="Z":
        hasUpper = True
    elif ch>="a" and ch<="z":
        hasLower = True
    elif ch>="0" and ch<="9":
        hasNum =True
    
if len(pw)>=8 and hasUpper and hasLower and hasNum:
    print("Your password is valid")
else:
    print("Invalid password!")