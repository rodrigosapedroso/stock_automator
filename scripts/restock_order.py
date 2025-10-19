file_stock = open('data/stock.csv', 'r')
init_stock = file_stock.read()
file_stock.close()
file_sales = open('data/sales.csv', 'r')
sales = file_sales.read()
file_sales.close()

from generate_stock import categories

def new_stock(stock, sales):

    title = 'item_name, category, restock\n'
    
    line_stock = stock.split('\n')
    stock_dict = {}
    for i in line_stock[1:-1]:
        stock_name = i.split(', ')[0]
        stock_quant = int(i.split(', ')[2])
        stock_min = int(i.split(', ')[3])
        stock_dict[stock_name] = [stock_quant, stock_min]

    line_sales = sales.split('\n')
    sales_dict = {}
    for i in line_sales[1:-1]:
        sales_name = i.split(', ')[0]
        sales_quant = int(i.split(', ')[2])
        sales_dict[sales_name] = sales_quant

    content = ''
    alert = False
    for nstock, qstock in stock_dict.items():
        for nsales, qsales in sales_dict.items():
            if nstock == nsales:
                for cat, name in categories.items():
                    if nstock in name:
                        category = cat
                        break
                stock = qstock[0]
                min_stock = qstock[1]
                available = stock - qsales
                if available <= min_stock:
                    restock = 2*min_stock - available
                    content += f'{nstock}, {category}, {restock}\n'
                    alert = True
   
    table = title + content
    return table, alert

def show_restock():

    restock, alert = new_stock(init_stock, sales)

    file_restock = open('data/restock.csv', 'w')
    file_restock.write(restock)
    file_restock.close()

    if alert:
        print('ALERT: New inventory to be restored!\n')
    else:
        print('No stock needed this week.\n')

    print(restock)

if __name__ == '__main__':
    show_restock()


    
    
    
