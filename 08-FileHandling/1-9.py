

# reads the entire file and splits lines into array

# Employee List

# Position
job_title = 'Software Engineer'

with open('it_company.csv') as file:
   for line in file:
      if job_title in line:
         print(line, end="")