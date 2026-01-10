test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

students_50_70 = list(filter(lambda s: 50 <= s["result"] <= 70, test_results))

print("Students with scores between 50 and 70:")
for student in students_50_70:
    print(student["name"])