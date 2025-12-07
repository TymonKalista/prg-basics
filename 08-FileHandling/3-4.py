import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of the email
with open(email_file) as file:
    email = file.read()

# regular expression pattern for amounts (e.g., €102, €30)
pattern = r'(\d+)'  # Capturing only the digits after the €

# extract numbers from email
amounts = re.findall(pattern, email)

# convert amounts to integers and sum them
total_spent = sum(map(int, amounts))

# print the result
print(total_spent)