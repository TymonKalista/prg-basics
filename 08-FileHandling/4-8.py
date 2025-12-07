import re
file_name = 'files.txt'
with open(file_name, 'r') as file:
    for line in file:
        if re.search(r'\.[a-zA-Z0-9]{4}$', line.strip()):
            print(line)
 
    