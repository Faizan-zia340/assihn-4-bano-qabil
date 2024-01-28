def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series

# Change the value of 'n' to the desired number of terms in the Fibonacci series
n = int(input("enter n number"))
result = fibonacci(n)

print(f"Fibonacci series with {n} terms: {result}")
