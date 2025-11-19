import random
import math
import time

def pollard_rho(n):
    start = time.time()  # Start timer

    if n % 2 == 0:
        print("Execution Time:", time.time() - start, "seconds")
        return 2  # If even, 2 is a factor

    # Choose random numbers
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    # Repeat until we find a factor
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = math.gcd(abs(x - y), n)

    print("Execution Time:", time.time() - start, "seconds")
    if d == n:
        return "Try again"
    else:
        return d


# Example
n = 8051  # 8051 = 83 * 97
print("A factor of", n, "is", pollard_rho(n))
