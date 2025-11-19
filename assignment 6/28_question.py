import time

def collatz_length(n):
    start = time.time()
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    end = time.time()
    print("Execution Time:", end - start, "seconds")
    return count

# Example
n = int(input("Enter a number: "))
print("Steps to reach 1:", collatz_length(n))
