import csv

with open('books.csv') as f:
    reader = csv.DictReader(f)
    books = []
    for row in reader:
        if row['Genre'] == 'Fantasy':
            x = [row['Title'], row['Author'], row['Genre'], row['Year']]
            books.append(x)
books_str = ""
for b in books:
    books_str += f"{b[0]}, {b[1]}, {b[2]}, {b[3]}\n"            
print(books_str)

with open('fantasy.txt', 'w') as file:
    file.write(books_str)


            
 

