import time

def lucas_sequence(n):
    start = time.time()
    a, b = 2, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    end = time.time()
    print("\nExecution Time:", end - start, "seconds")

# Example
n = int(input("Enter number of terms: "))
lucas_sequence(n)
