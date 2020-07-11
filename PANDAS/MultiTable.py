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

sales = pd.read_csv('sales.csv')

targets = pd.read_csv('targets.csv')

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets)\
	.merge(men_women)

print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

rders_products = pd.merge(
	orders,
	products.rename(columns={'id':'product_id'})
)
print(orders_products)

orders_products = pd.merge(
	orders,
	products,
	left_on = 'product_id',
	right_on = 'id',
	suffixes = ['_orders', '_products']
)

print(orders_products)

print(orders)
print(products)

merged_df = pd.merge(orders, products)

print(merged_df)

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')

print(store_a_b_outer)

store_a_b_left = pd.merge(store_a, store_b, how='left')
store_b_a_left = pd.merge(store_b, store_a, how='left')

print(store_a_b_left)
print(store_b_a_left)

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

# Concatenate the two menus to form a new menu
menu = pd.concat([bakery, ice_cream])

print(menu)

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

# Part 1: print to inspect each DataFrame
print(visits.head(10))
print(checkouts.head(10))

# Part 2: merge visits and checkouts
v_to_c = pd.merge(visits, checkouts)

# Part 3: define the column time to be the different between checkout time and visit time
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time

print(v_to_c.time.mean())