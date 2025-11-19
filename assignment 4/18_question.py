import time

def multiplicative_persistence(n):
    start = time.time()
    count = 0
    while n > 9:
        p = 1
        for d in str(n):
            p = p * int(d)
        n = p
        count = count + 1
    end = time.time()
    print("Execution time:", end - start, "seconds")
    return count

# Example
num = int(input("Enter a number: "))
print("Multiplicative persistence is", multiplicative_persistence(num))


