import time

def count_distinct_prime_factors(n):
    start = time.time()  # Start timing
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1  # n itself is a prime
    end = time.time()  # End timing
    print(f"Execution time: {end - start:.6f} seconds")
    return count

# Example usage
num = 60
print(f"Distinct prime factors of {num}: {count_distinct_prime_factors(num)}")