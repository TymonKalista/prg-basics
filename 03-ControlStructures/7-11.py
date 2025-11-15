current_product_price = 140
previous_product_price = 200
percent = ((previous_product_price - current_product_price)/previous_product_price)*100
if percent >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {percent:g}%')