import time

def count_divisors(n):
    start = time.time()
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                divisors += 1  # perfect square counts once
            else:
                divisors += 2  # count both divisor and pair
    end = time.time()
    return divisors, end - start

# Example:
count, t = count_divisors(36)
print("Number of divisors:", count)
print("Time taken:", t)

