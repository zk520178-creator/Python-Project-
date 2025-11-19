import time

def mod_exp(base, exp, mod):
    start = time.time()
    result = 1
    for i in range(exp):
        result = (result * base) % mod
    end = time.time()
    print("Execution time:", end - start, "seconds")
    return result

# Example
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
m = int(input("Enter modulus: "))

print("Result:", mod_exp(b, e, m))
