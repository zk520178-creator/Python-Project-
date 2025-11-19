import time

def is_perfect_power(n):
    start = time.time()
    for a in range(2, n):
        for b in range(2, n):
            if a ** b == n:
                print("Execution Time:", time.time() - start, "seconds")
                return True
            if a ** b > n:
                break
    print("Execution Time:", time.time() - start, "seconds")
    return False

# Example
n = int(input("Enter a number: "))
if is_perfect_power(n):
    print(n, "is a Perfect Power.")
else:
    print(n, "is NOT a Perfect Power.")
