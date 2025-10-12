import random

categories = {'Tops': ["T-Shirt", "Blouse", "Shirt", "Sweater", "Tank Top"],
    'Bottoms': ["Jeans", "Trousers", "Shorts", "Skirt"],
    'Outerwear': ["Jacket", "Coat", "Hoodie", "Blazer"], 
    'Dresses': ["Dress", "Gown", "Jumpsuit"],
    'Footwear': ["Sneakers", "Boots", "Sandals", "Heels"],
    'Accessories': ["Belt", "Scarf", "Hat", "Bag", "Sunglasses"]}

def generate_initial_stock(num_lines):

    stock_content = ''
    for _ in range(num_lines):
        category = random.choice(list(categories.keys()))
        name = random.choice(categories[category])
        if category == 'Tops' or category == 'Bottoms':
            stock = random.randint(10, 20)
            min_stock = 5
        elif category == 'Outerwear' or category == 'Dresses':
            stock = random.randint(5, 10)
            min_stock = 3
        elif category == 'Footwear' or category == 'Accessories':
            stock = random.randint(8, 15)
            min_stock = 2
        stock_content += f'{name}, {category}, {stock}, {min_stock}\n'

    stock_title = 'item_name, category, stock, min_stock\n'
    table = stock_title + stock_content
    return table

stock_table = generate_initial_stock(100)
print(stock_table)

file = open('data/stock.csv', 'w')
file.write(stock_table)