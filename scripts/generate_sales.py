from generate_stock import categories
import random

sales_title = 'item_name, category, sales\n'

def generate_sales(num_lines):
    sales_table = ''
    for _ in range(num_lines):
        category = random.choice(list(categories.keys()))
        name = random.choice(categories[category])
        sales = random.randint(2, 20)
        sales_table += f'{name}, {category}, {sales}\n'

    return sales_title + sales_table

def sum_sales(sales_table):
    
    line_sales = sales_table.split('\n')
    quant_list_sales = []
    for i in line_sales[1:-1]:
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

    return total_sales

file_stock = open('data/stock.csv', 'r')
stock_table = file_stock.read()
file_stock.close()

def sum_stock(stock_table):
    line_stock = stock_table.split('\n')
    quant_list_stock = []
    for i in line_stock[1:-1]:
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

    return total_stock

sales_table = generate_sales(100)
print(sales_table)
total_sales = sum_sales(sales_table)
print(total_sales)
total_stock = sum_stock(stock_table)
print(total_stock)

def fix_sales(total_sales, total_stock):
    
    new_total_sales = {}
    for nsales, qsales in total_sales.items():
        for nstock, qstock in total_stock.items():
            if nstock == nsales:
                if int(qstock) < int(qsales):
                    new_total_sales[nsales] = qstock
                else:
                    new_total_sales[nsales] = qsales
    
    sales_table = ''
    for n, q in new_total_sales.items():
        for cat, l in categories.items():
            if n in l:
                category = cat

        sales_table += f'{n}, {category}, {q}\n'

    return sales_title + sales_table

sales_table = fix_sales(total_sales, total_stock)
print(sales_table)

file_sales = open('data/sales.csv', 'w')
file_sales.write(sales_table)
file_sales.close()