from generate_stock import categories
import random

def generate_sales(num_lines):
    sales_title = 'item_name, category, sales\n'
    sales_table = ''
    for _ in range(num_lines):
        category = random.choice(list(categories.keys()))
        name = random.choice(categories[category])
        sales = random.randint(2, 20)
        sales_table += f'{name}, {category}, {sales}\n'

    return sales_title + sales_table

sales_table = generate_sales(100)
print(sales_table)