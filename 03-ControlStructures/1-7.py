###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.3 
is_bonus = input('Does the employee receive a bonus? (Y/N):') 

if is_bonus == 'N':
    total_salary = basic_salary
else:
    total_salary = basic_salary + basic_salary*bonus

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {total_salary}')
print(f'Total salary: {total_salary}')