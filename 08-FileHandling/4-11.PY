file_name ='powers_of_1-100'
with open(file_name, 'w') as file:
    for i in range(1,101):
        file.write(f'{i},{i*i}, {i*i*i}\n')
