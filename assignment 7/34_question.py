import time

def partition_function(n):
    start = time.time()  # start timer

    # Base case
    ways = [0] * (n + 1)
    ways[0] = 1

    # Count partitions
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ways[j] = ways[j] + ways[j - i]

    print("Execution Time:", time.time() - start, "seconds")
    return ways[n]


# Example
n = 5
print("Number of partitions of", n, "is", partition_function(n))
