import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)

print(products)

print(customers)

order_3_description = 'thing-a-ma-jig'
order_5_phone_number = '112-358-1321'


sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)

print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]