import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
    'Salary': [70000, 80000, 65000, 60000, 90000]
}

df = pd.DataFrame(data)

# Filter employees with salary > 65000
filtered = df[df['Salary'] > 65000]

# Group by Department, calculate average salary
grouped = df.groupby('Department')['Salary'].mean()

print("Filtered Employees:\n", filtered)
print("\nAverage Salary by Department:\n", grouped)
