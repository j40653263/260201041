gpa = float(input("Enter your GPA: "))
numberOfLecture = int(input("Enter number of lecture: "))

if gpa<2.0:
  if numberOfLecture<47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if numberOfLecture<47:
    print("Not enough number of lectures!")
  else:
    print("GRADUATED!!!")
