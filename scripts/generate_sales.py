from generate_stock import categories
import random

sales_title = 'item_name, category, sales\n'

def create_sales(num_lines):

    table = ''
    for _ in range(num_lines):
        category = random.choice(list(categories.keys()))
        name = random.choice(categories[category])
        sales = random.randint(2, 20)
        table += f'{name}, {category}, {sales}\n'

    return table

def fix_sales(sales, stock):
    
    line_sales = sales.split('\n')
    quant_list_sales = []
    for i in line_sales[:-1]:
        name = i.split(', ')[0]
        quant = int(i.split(', ')[2])
        quant_list_sales.append({name: quant})
    
    total_sales = {}
    for i in quant_list_sales: 
        for n, q in i.items():
            if n in total_sales:
                total_sales[n] += q
            elif n not in total_sales:
                total_sales[n] = q

    line_stock = stock.split('\n')
    total_stock = {}
    for i in line_stock[1:-1]:
        name = i.split(', ')[0]
        quant = int(i.split(', ')[2])
        total_stock[name] = quant
    
    new_total_sales = {}
    for nsales, qsales in total_sales.items():
        for nstock, qstock in total_stock.items():
            if nstock == nsales:
                if int(qstock) < int(qsales):
                    new_total_sales[nsales] = qstock
                else:
                    new_total_sales[nsales] = qsales
    
    sales_content = ''
    for n, q in new_total_sales.items():
        for cat, l in categories.items():
            if n in l:
                category = cat

        sales_content += f'{n}, {category}, {q}\n'

    table = sales_title + sales_content
    return table

raw_table = create_sales(100)
file_stock = open('data/stock.csv', 'r')
stock_table = file_stock.read()
file_stock.close()
sales_table = fix_sales(raw_table, stock_table)
print(sales_table)

file_sales = open('data/sales.csv', 'w')
file_sales.write(sales_table)
file_sales.close()