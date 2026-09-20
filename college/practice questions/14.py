Basic_salary = float(input("Enter the Basic salary (per month): "))
H_R_A = float(input("Enter the Housing Rent Allowance:  "))
Gross_Salary = float(input("Enter the Gross salary of the employee (per month):  "))
Monthly_Salary = Basic_salary+H_R_A+Gross_Salary
print("The monthly salary of the employee is:  ", Monthly_Salary)
Annual_Salary = Monthly_Salary*12
print("The Annual Salary of the employee is:   ", Annual_Salary)