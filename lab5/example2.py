grades = [[50,90,60],[15,60,75],[99,95,91]]
aa = []
average = []
for i in range(len(grades)):
    student = grades[i]
    grade = student[0]*0.3 + student[1]*0.3 + student[2]*0.4
    average.append(grade)
    if grade >= 90:
        aa.append(i)

print("Average grades are:",average)
print("AA students:")
for i in aa:
    print(i)