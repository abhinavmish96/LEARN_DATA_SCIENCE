import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive = orders.price.max()
num_colors = orders.shoe_color.nunique()

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index();

print(pricey_shoes)

print(type(pricey_shoes))

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()

print(cheap_shoes)