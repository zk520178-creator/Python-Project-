import time   # to measure time

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Take number from user
num = int(input("Enter a number: "))

start = time.time()      # start time
ans = factorial(num)     # call function
end = time.time()        # end time

print("Factorial of", num, "is:", ans)
print("Execution time:", end - start, "seconds")

# time complexity = O(n)