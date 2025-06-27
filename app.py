def fibonacci_series(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get number of terms from user
try:
    n = int(input("Enter number of the Fibonacci terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci series:", fibonacci_series(n))
except ValueError:
    print("Invalid input. Please enter a number.")
