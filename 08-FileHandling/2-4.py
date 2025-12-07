###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

with open(employees_file) as file:
      content = file.read()

# Position
job_title = 'Software Engineer'

contnent = content.splitlines()
if job_title in content:
      print(content)
    


#write selected employees to a file
#with open(employees_file, 'r') as employees:
  #  with open(position_file, 'w') as engeeneers:
 #     for line in employees:
   #      if job_title in line:
    #        engeeneers.write(line)