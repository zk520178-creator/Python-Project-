import random
import time

def is_prime_miller_rabin(n, k=5):
    start = time.time()   # Start timing

    # Handle small numbers
    if n <= 1:
        print("Execution Time:", time.time() - start, "seconds")
        return False
    if n <= 3:
        print("Execution Time:", time.time() - start, "seconds")
        return True
    if n % 2 == 0:
        print("Execution Time:", time.time() - start, "seconds")
        return False

    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Repeat k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n

        if x == 1 or x == n - 1:
            continue

        flag = False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                flag = True
                break

        if not flag:
            print("Execution Time:", time.time() - start, "seconds")
            return False  # Not prime

    print("Execution Time:", time.time() - start, "seconds")
    return True  # Probably prime


# Example
n = 97
print(n, "is prime?", is_prime_miller_rabin(n, 5))
