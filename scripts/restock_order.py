from generate_stock import categories

def new_stock(stock, sales):

    title = 'item_name, category, restock\n'
    
    line_stock = stock.split('\n')
    stock_dict = {}
    for i in line_stock[1:-1]:
        stock_name = i.split(', ')[0].strip()
        stock_quant = int(i.split(', ')[2])
        stock_min = int(i.split(', ')[3])
        stock_dict[stock_name] = [stock_quant, stock_min]

    line_sales = sales.split('\n')
    sales_dict = {}
    for i in line_sales[1:-1]:
        sales_name = i.split(', ')[0].strip()
        sales_quant = int(i.split(', ')[2])
        sales_dict[sales_name] = sales_quant

    content = ''
    alert = False
    for nstock, qstock in stock_dict.items():
        qsales = sales_dict.get(nstock.strip(), 0)
        stock = qstock[0]
        min_stock = qstock[1]
        available = stock - qsales
        if available <= min_stock:
            restock = 2 * min_stock - available
            for cat, name in categories.items():
                    if nstock in name:
                        category = cat
                        break
            content += f'{nstock}, {category}, {restock}\n'
            alert = True
   
    table = title + content
    return table, alert, stock_dict, sales_dict

def warn_min(stock_dict, sales_dict):

    content = []
    alert = False
    for nstock, qstock in stock_dict.items():
        qsales = sales_dict.get(nstock.strip(), 0)
        stock = qstock[0]
        min_stock = qstock[1]
        available = stock - qsales
        if min_stock < available < (1.5*min_stock):
            content.append(nstock)
            alert = True

    content = ', '.join(content) 
    return content, alert

def show_restock(init_stock, sales):

    restock, alert2, stock_dict, sales_dict = new_stock(init_stock, sales)
    items, alert1 = warn_min(stock_dict, sales_dict)

    if alert1:
        print(f'ATTENTION! Stock is approaching minimum for the following item(s): {items}\n')

    if alert2:
        print('ALERT: New inventory to be restored!\n')
    else:
        print('No stock needed this week.\n')

    print(restock)

    file_restock = open('data/restock.csv', 'w')
    file_restock.write(restock)
    file_restock.close()

    return restock
