import pandas as pd

data = {'Name': ['Luther', 'Martin'], 'Age': [25, 30], 'Country': ['JAPAN', 'EUROPE'], 'Salary':
    [600000, 75000]}
df = pd.DataFrame(data)
print("\nInitial DataFrame:\n", df)
print("\nName column:\n", df['Name'])
print("\nAge column:\n", df['Age'])
df['Experience'] = [13, 5]
df.loc[0, 'Age'] = 29
df.at[1, 'Country'] = 'Australia'
df.drop('Salary', axis=1, inplace=True)
filtered_data = df[df['Age'] > 25]
sorted_data = df.sort_values(by='Age')
print("\nModified DataFrame: \n", df)
print("\nFiltered DataFrame: \n", filtered_data)
print("\nSorted DataFrame: \n", sorted_data)