mail = input("Enter an email: ")
mail=mail.lower()
target = "ceng113@example.com"

index_of_at = mail.index("@")
mail_before_at = mail[0:index_of_at]
mail_after_at = mail[index_of_at:]

mail_before_at = mail_before_at.replace(".","")
mail = mail_before_at + mail_after_at

if mail == target:
    print("It is correct email address.")
else:
    print("It is wrong!")