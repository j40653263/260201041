class Employee:   
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
    
  def get_name(self):
    return self.name
    
  def set_name(self,name):
    self.name = name 
      
  def get_salary(self):
    return self.salary
  
  def set_salary(self,salary):
    if salary > 0:
      self.salary = salary  
          
  def display(self):
    print("Name " + self.name + ", Salary" , self.salary)

  
class Company:  
  def __init__(self):
    self.employee_list = []
      
  def get_employee_list(self):
    return self.employee_list
  
  def set_emp_list(self,employee_list):
    if isinstance(employee_list , list):
      self.employee_list = employee_list
          
  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      self.employee_list.append(new_employee)
          
  def calc_average_salary(self):
    total_salary = 0
    for emp in self.employee_list:
      total_salary += emp.get_salary()
          
    return total_salary/len(self.employee_list)

  def display_employees(self):
    for emp in self.employee_list:
      print(emp.display())
            
e1 = Employee("A",3000)
e2 = Employee("B",8000)
e3 = Employee("C",4000)
e = [e1,e2,e3]
c = Company()
c.set_emp_list(e)
c.display_employees()
print("Average salary:",c.calc_average_salary())