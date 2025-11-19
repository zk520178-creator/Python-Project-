import time

def aliquot_sum(n):
    start = time.time()  # Start timer
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    end = time.time()  # End timer
    print("Execution time:", end - start, "seconds")
    return total

# Example
num = int(input("Enter a number: "))
print("Aliquot sum of", num, "is", aliquot_sum(num))
