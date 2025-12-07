file_name = (input('eNTER YOUR FILE NAME: '))

with open(file_name, 'r') as file:
    omunt_of_lines = 0
    for line in file:
        omunt_of_lines = omunt_of_lines + 1
print(omunt_of_lines)

with open(file_name, 'r') as file:
    content = file.read()
    amount_of_words = 0
    content = content.replace(',', " ")
    x = content.split()
    y = len(x)
print(y)

with open(file_name, 'r') as file:
    content = file.read()
    content = content. replace('',' ')
    z = content.split()
    u = len(z)
print(u)


    