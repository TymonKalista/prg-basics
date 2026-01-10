from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Function to add two numbers
result = reduce(lambda x,y: x+y, numbers)


#
print(result)  # Output: 15