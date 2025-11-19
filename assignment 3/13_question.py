import time

def is_mersenne_prime(p):
    start = time.time()

    # Check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check p prime
    if not is_prime(p):
        return False, 0

    mersenne = 2**p - 1

    # Check if mersenne number is prime
    result = is_prime(mersenne)

    end = time.time()
    return result, end - start

# Example usage:
answer, time_taken = is_mersenne_prime(7)
print("Mersenne prime?", answer)
print("Time taken:", time_taken)
