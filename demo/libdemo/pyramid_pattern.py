rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("* " * i)