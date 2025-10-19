from generate_stock import show_stock
from generate_sales import show_sales
from restock_order import show_restock

stock = show_stock(100) #input = number of initial stock random lines (example: 100)
sales = show_sales(100) #input = number of initial sales random lines (example: 100)
show_restock(stock, sales)