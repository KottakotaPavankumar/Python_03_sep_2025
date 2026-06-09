import statistics

numbers = input("Enter a list of numbers (space-separated): ").split()
numbers = list(map(float, numbers))
mean = sum(numbers) / len(numbers)
mode = statistics.mode(numbers)
median = statistics.median(numbers)
variance = statistics.variance(numbers)
std_deviation = statistics.stdev(numbers)
print("\nMean:", mean)
print("\nMode:", mode)
print("\nMedian:", median)
print("\nVariance:", variance)
print("\nStandard Deviation:", std_deviation)
