import json
product = {}
product['name'] = (input('Enter product name: '))
price_str = input("Enter product price (e.g. 12.50): ")
product['price'] = float(price_str)   

paid_str = input("Was the product paid? (yes/no): ").strip().lower()


if paid_str == "yes":
    product['paid'] = True
else:
    product['paid'] = False


with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print("Product data saved to product.json")