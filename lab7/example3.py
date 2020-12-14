employees = {}
for i in range(5):
  name = input("Enter name: ")
  salary = int(input("Enter salary: "))
  employees[name] = salary 

salary_list = []
for i in employees.values():
  salary_list.append(i)
salary_list.sort()
for k,v in employees.items():
  if v in salary_list[-3:]:
    print(k)

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