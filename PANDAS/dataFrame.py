import pandas as pd


df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt','t-shirt','skirt','skirt'],
  'Color': ['blue','green','red','black']
})

print(df1)

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
  ],
  columns=['Store ID', 'Location','Number of Employees'])

print(df2)

df = pd.read_csv('sample.csv')

print(df)

df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north

print(type(clinic_north))

print(type(df))

clinic_north_south = df[['clinic_north', 'clinic_south']]

print(type(clinic_north_south))

march = df.iloc[2]

april_may_june = df.iloc[3:]

print(april_may_june)

january = df[df.month == 'January']

print(january)

march_april = df[(df.month == 'March') | (df.month == 'April')]

print(march_april)

df2 = df.loc[[1, 3, 5]]


df3 = df2.reset_index()

print(df3)

df2.reset_index(inplace = True, drop = True)

print(df2)

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df['Sold in Bulk?'] = ['Yes','Yes','No','No']
df['Is taxed?'] = 'Yes'
df['Margin'] = df['Price'] - df['Cost to Manufacture']

print(df)

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

df['Lowercase Name'] = df.Name.apply(lower)
print(df)