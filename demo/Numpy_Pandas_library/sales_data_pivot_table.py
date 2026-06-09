import pandas as pd

data = {
    'Date': pd.date_range('2025-06-01', periods=8),
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['East', 'East', 'West', 'West', 'East', 'East', 'West', 'West'],
    'Sales': [200, 150, 300, 250, 180, 160, 310, 270]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum')

print(pivot)
