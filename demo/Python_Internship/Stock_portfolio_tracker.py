
# ✅ TASK 2: Stock Portfolio Tracker


# Hardcoded stock prices (you can add more)
stock_prices = {
    "AAPL": 180,    # Apple
    "TSLA": 250,    # Tesla
    "GOOGL": 140,   # Google
    "AMZN": 130,    # Amazon
    "MSFT": 320     # Microsoft
}

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices (per share):")
for stock, price in stock_prices.items():
    print(f"   {stock}: ${price}")

portfolio = {}  # To store user-entered stocks and quantities

# Step 1: Take user input
while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("⚠ Stock not found in list. Please enter a valid symbol (e.g., AAPL, TSLA).")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name} shares: "))
        if quantity <= 0:
            print("⚠ Quantity must be positive.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("⚠ Please enter a valid number for quantity.")

# Step 2: Calculate total investment
total_value = 0
print("\n💹 Your Portfolio Summary:")
print("------------------------------")

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print("------------------------------")
print(f"💰 Total Investment Value: ${total_value}")

# Step 3 (Optional): Save result to file
save = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("------------------------\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        f.write("------------------------\n")
        f.write(f"Total Investment Value: ${total_value}\n")
    print("✅ Portfolio saved successfully to 'portfolio_summary.txt'")

print("\n📊 Thank you for using the Stock Portfolio Tracker!")


"""
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 315,
    "AMZN": 120
}

portfolio = {}

# Input stocks and quantities
print("Enter your stock holdings.")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when finished.
")

while True:
    stock = input("Stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from available stocks.
")
        continue
    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Please enter a valid integer quantity.
")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = 0
print("
Your Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
    total_investment += value

print(f"
Total Investment Value: ${total_investment}")

# Optionally save result to a file
save_choice = input("Do you want to save this result to a file? (yes/no): ").lower()
if save_choice == "yes":
    filename = "portfolio.txt"
    with open(filename, "w") as f:
        f.write("Stock Portfolio Holdings
")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}
")
        f.write(f"
Total Investment Value: ${total_investment}
")
    print(f"Result saved to {filename}")
"""