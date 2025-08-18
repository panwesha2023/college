#A company offers the bonus as 25% of salary if an employee is a manager otherwise bonus is 7%of salary.print the gross salary.
desig = input("Enter the designation ")
sal = int(input("Enter the salary "))
bonus = 0
gs = 0
if(desig == "manager"):
  bonus = sal * 25 / 100
else:
  bonus = sal * 7 / 100
gs = sal + bonus
print("gross salary= ",gs)
