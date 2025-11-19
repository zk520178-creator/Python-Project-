import time

def twin_primes(limit):
    start = time.time()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            result.append((num, num + 2))

    end = time.time()
    return result, end - start

# Example:
pairs, t = twin_primes(20)
print("Twin primes:", pairs)
print("Time taken:", t)
