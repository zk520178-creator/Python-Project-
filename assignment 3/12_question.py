import time

def is_prime_power(n):
    start = time.time()
    if n <= 1:
        return False, 0
    
    # Check if a number is prime
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime(p):
            power = p
            while power < n:
                power *= p
            if power == n:
                end = time.time()
                return True, end - start
    
    end = time.time()
    return False, end - start

# Example:
result, t = is_prime_power(27)
print("Prime power?", result)
print("Time taken:", t)
