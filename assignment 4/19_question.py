import time

def count_divisors(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count

def is_highly_composite(n):
    n_div = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= n_div:
            return False
    return True

n = int(input("Enter a number: "))
start = time.time()
result = is_highly_composite(n)
end = time.time()

print("Is highly composite?", result)
print("Execution time:", end - start, "seconds")
