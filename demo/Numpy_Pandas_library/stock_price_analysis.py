import numpy as np
import pandas as pd

# Sample stock prices data with dates
dates = pd.date_range('2025-01-01', periods=10)
prices = np.array([100, 102, 101, 105, 110, 108, 107, 111, 115, 117])

df = pd.DataFrame({'Date': dates, 'Price': prices})
df.set_index('Date', inplace=True)

# Calculate 3-day moving average using NumPy's convolve
moving_avg = np.convolve(df['Price'], np.ones(3)/3, mode='valid')

df['3-day MA'] = np.nan
df['3-day MA'].iloc[2:] = moving_avg

print(df)
