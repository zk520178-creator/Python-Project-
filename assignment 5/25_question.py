import time
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    s1 = int(math.sqrt(x1))
    s2 = int(math.sqrt(x2))
    return s1 * s1 == x1 or s2 * s2 == x2

def is_fibonacci_prime(n):
    start = time.time()
    if is_prime(n) and is_fibonacci(n):
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return True
    else:
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return False

# Example
n = int(input("Enter a number: "))

if is_fibonacci_prime(n):
    print(n, "is a Fibonacci Prime number.")
else:
    print(n, "is NOT a Fibonacci Prime number.")
