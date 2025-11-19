import time

def aliquot_sum(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return s

def are_amicable(a, b):
    start = time.time()
    if aliquot_sum(a) == b and aliquot_sum(b) == a:
        print("They are amicable numbers")
    else:
        print("They are not amicable numbers")
    end = time.time()
    print("Execution time:", end - start, "seconds")

# Example
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
are_amicable(a, b)
