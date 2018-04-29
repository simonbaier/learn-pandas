import pandas as pd
df = pd.read_csv('UdemyPandas/data/chicago.csv').dropna(how='all')
# df.head()

# count most popular first names
# first = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ').str.get(0).value_counts()
# type(first)
# note that first is a series with the name as the index

# first.head()

# split Names and add first and last name columns
df['Name'].str.split(',', expand = True).head()

#now add the first and last names to the end of the original dataframe
df[['Last Name','First Name']] = df['Name'].str.split(',', expand = True)

df['First Name'] = df['First Name'].str.strip().str.title()
df['Last Name'] = df['Last Name'].str.strip().str.title()

search_string = 'bAi'
mask = df['Last Name'].str.upper().str.startswith(search_string.upper())
df[mask]
print(search_string)
