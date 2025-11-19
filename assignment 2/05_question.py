import time

def is_abundant(n):
    start = time.time()  # Start timing

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    end = time.time()  # End timing
    print("Execution time:", end - start, "seconds")
    return total > n

# Example
print("Is abundant:", is_abundant(12))  # Output: True

# TIME complexity =  O(n)
