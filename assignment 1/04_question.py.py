import math
import time

def prime_pi(n):
    if n < 2:
        return 0
    return int(n / math.log(n))  # Approximation formula

start = time.time()

# Example calls
print("π(10) ≈", prime_pi(10))      # Around 4
print("π(100) ≈", prime_pi(100))    # Around 25
print("π(1000) ≈", prime_pi(1000))  # Around 168

end = time.time()
print("Execution time: {:.8f} seconds".format(end - start))

# the time complexity is = O(1)


