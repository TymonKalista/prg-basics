
file_name = 'tymon.txt'
x = input('Enter your vowel: ')
with open(file_name, 'r') as file:
    content = file.read()
    content= content.lower()
    y = content.count(x)
print(y)



