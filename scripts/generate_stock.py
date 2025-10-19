import random

categories = {'Tops': ["T-Shirt", "Blouse", "Shirt", "Sweater", "Tank Top"],
    'Bottoms': ["Jeans", "Trousers", "Shorts", "Skirt"],
    'Outerwear': ["Jacket", "Coat", "Hoodie", "Blazer"], 
    'Dresses': ["Dress", "Gown", "Jumpsuit"],
    'Footwear': ["Sneakers", "Boots", "Sandals", "Heels"],
    'Accessories': ["Belt", "Scarf", "Hat", "Bag", "Sunglasses"]}

stock_title = 'item_name, category, stock, min_stock\n'

def create_stock(num_lines):

    table = ''
    for _ in range(num_lines):
        category = random.choice(list(categories.keys()))
        name = random.choice(categories[category])
        if category == 'Tops' or category == 'Bottoms':
            stock = random.randint(10, 20)
        elif category == 'Outerwear' or category == 'Dresses':
            stock = random.randint(5, 10)
        elif category == 'Footwear' or category == 'Accessories':
            stock = random.randint(8, 15)
        table += f'{name}, {category}, {stock}\n'

    return table

def resume_stock(table):

    line_stock = table.split('\n')
    quant_list_stock = []
    for i in line_stock[:-1]:
        name = i.split(', ')[0]
        quant = int(i.split(', ')[2])
        quant_list_stock.append({name: quant})

    total_stock = {}
    for i in quant_list_stock: 
        for n, q in i.items():
            if n in total_stock:
                total_stock[n] += q
            elif n not in total_stock:
                total_stock[n] = q
    
    stock_content = ''
    for n, q in total_stock.items():
        for cat, l in categories.items():
            if n in l:
                category = cat
                break
        if category == 'Tops' or category == 'Bottoms':
            min_stock = 10
        elif category == 'Outerwear' or category == 'Dresses':
            min_stock = 8
        elif category == 'Footwear' or category == 'Accessories':
            min_stock = 6

        stock_content += f'{n}, {category}, {q}, {min_stock}\n'

    table = stock_title + stock_content
    return table

def show_stock(num_lines):

    title = '\nSTOCK\n\n'
    raw_table = create_stock(num_lines)
    stock_table = resume_stock(raw_table)
    print(title + stock_table)

    file = open('data/stock.csv', 'w')
    file.write(stock_table)
    file.close()

    return stock_table

if __name__ == '__main__':
    show_stock(100)