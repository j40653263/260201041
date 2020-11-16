pw = input("Enter password: ")
correctPw = "abc123"

while True:
    if pw == correctPw:
        print("Welcome!")
        break
    elif pw == "help":
        print(correctPw[0])
        pw = input("Enter password: ")
    else:
        print("Wrong")
        pw = input("Enter password: ")