import keyboard 

first_name = keyboard.input_string('Enter name: ')
last_name =keyboard. input_string('Enter last name: ')
age = keyboard.input_integer('Enter your age: ')
salary = keyboard.input_real('Enter your salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname', last_name)
print('Age: ', age)

if is_salary_hidden:
    print('Salary: ', salary)
else:
    print('Salary: [hidden]')



