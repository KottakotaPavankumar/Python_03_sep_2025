n = int(input("Enter the number of data points: "))
x = [float(input(f"Enter x value {i + 1}: ")) for i in range(n)]
y = [float(input(f"Enter y value {i + 1}: ")) for i in range(n)]
m_x, m_y = sum(x) / n, sum(y) / n
p = sum((x[i] - m_x) * (y[i] - m_y) for i in range(n)) / (sum((x[i] - m_x) ** 2 for i in
                                                              range(n)) ** 0.5 * sum(
    (y[i] - m_y) ** 2 for i in range(n)) ** 0.5)
r_x, r_y = [sorted(x).index(v) + 1 for v in x], [sorted(y).index(v) + 1 for v in y]
r = 1 - 6 * sum((r_x[i] - r_y[i]) ** 2 for i in range(n)) / (n * (n ** 2 - 1))
print("Pearson Correlation:", p)
print("Rank Correlation:", r)
