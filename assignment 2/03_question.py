import time   # to measure time

def mean_of_digits(n):
    total = 0
    count = 0
    while n > 0:
        total = total + (n % 10)   # add last digit
        count = count + 1          # count digits
        n = n // 10                # remove last digit
    return total / count           # find average

# Take number from user
num = int(input("Enter a number: "))

start = time.time()                # start time
mean = mean_of_digits(num)         # function call
end = time.time()                  # end time

print("Mean of digits is:", mean)
print("Execution time:", end - start, "seconds")

# time complexity = O(logn)