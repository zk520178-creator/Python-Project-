import time

def legendre_symbol(a, p):
    symbol = pow(a, (p-1)//2, p)  # Euler's criterion
    if symbol == p - 1:
        return -1
    else:
        return symbol

start = time.time()
a, p = 5, 7  # Example values: odd prime p, a not divisible by p
result = legendre_symbol(a, p)
end = time.time()

print(f"Legendre symbol ({a}/{p}) =", result)
print("Execution time:", end-start, "seconds")

 # the time complexity is = O(logp)