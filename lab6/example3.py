employees = {}
for i in range(5):
    name = input("Enter the employees name: ")
    salary = int(input("Enter his/her salary: "))
    employees[name] = salary 

salary_list = []
for v in employees.values():
    salary_list.append(v)

salary_list.sort()
x1 = salary_list[-1]
x2 = salary_list[-2]
x3 = salary_list[-3]

for k in employees.keys():
    if employees[k] == x1:
        print(k,x1,"Highest")
    
    if employees[k] == x2:
        print(k,x2,"Second")
    
    if employees[k] == x3:
        print(k,x3,"Third")

""""
employees = dict()
for _ in range(5):
    name = input("Enter name:")
    salary = int(input("Enter salary:"))
    employees[name] = salary
# Names are not necessarily sorted by their salaries. (We didn't explicitly say this)
# We can print them in any order as long as they are the top 3.
best_three_salaries = sorted(employees.values())[-3:]
for name in employees.keys():
    salary = employees[name]
    if salary in best_three_salaries:
        print(name)
# Alternatively
# for name in employees:
#   salary = employees[name]
#   if salary in best_three_salaries:
#       print(name)
# Alternatively
# for name, salary in employees.items():
#   if salary in best_three_salaries:
#       print(name)
"""