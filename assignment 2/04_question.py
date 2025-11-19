import time

def digital_root(n):
    start = time.time()
    n = abs(n)  # Make sure the number is positive
    while n > 9:
        n = sum(int(d) for d in str(n))
    end = time.time()
    return n, end - start

# Example usage
result, exec_time = digital_root(9455)
print("Digital root:", result)
print("Execution time:", exec_time, "seconds")

#  Time Complexity: O(log n)
