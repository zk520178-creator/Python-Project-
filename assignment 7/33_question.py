import time

def zeta_approx(s, terms):
    start = time.time()  # start timer

    sum = 0
    for n in range(1, terms + 1):
        sum = sum + 1 / (n ** s)

    print("Execution Time:", time.time() - start, "seconds")
    return sum


# Example
s = 2
terms = 1000
print("Zeta(", s, ") ≈", zeta_approx(s, terms))
