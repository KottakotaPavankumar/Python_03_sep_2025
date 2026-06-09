print("The perfect numbers from 1 to 1000 are:")
print(1, end=' ')  # Including 1 as per your requirement

for n in range(2, 1001):
    total = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            total += i  # add factor

    if total == n:
        print(n, end=' ')
