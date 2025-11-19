import time

def divisor_sum(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

n = 10000  # Pick any number you want

start = time.time()     # start timing here
result = divisor_sum(n)
end = time.time()       # end timing here

print("Sum of divisors of", n, "is:", result)
print("Execution time:", end - start, "seconds")



# the time complexity is =  O(n).

