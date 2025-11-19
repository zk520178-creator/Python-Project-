import time

def mobius(n):
    if n == 1:
        return 1  # μ(1) = 1 by definition
    prime_factors = {}
    temp = n
    factor = 2
    while factor * factor <= temp:
        count = 0
        while temp % factor == 0:
            temp //= factor
            count += 1
        if count > 0:
            prime_factors[factor] = count
        factor += 1
    if temp > 1:
        prime_factors[temp] = 1
    if any(count > 1 for count in prime_factors.values()):
        return 0
    num_primes = len(prime_factors)
    return 1 if num_primes % 2 == 0 else -1

def mobius_with_time(n):
    start = time.time()
    result = mobius(n)
    end = time.time()
    exec_time = end - start
    return result, exec_time

# Example usage
test_number = 30
value, execution_time = mobius_with_time(test_number)
print("μ({}) = {}, execution time = {:.8f} seconds".format(test_number, value, execution_time))

# The time complexity is = O(√nlogn)
