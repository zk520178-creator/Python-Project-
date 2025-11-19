import time

def is_quadratic_residue(a, p):
    # Euler's criterion: a^((p-1)//2) mod p == 1 means a is a quadratic residue mod p
    return pow(a, (p-1)//2, p) == 1

start = time.time()
result = is_quadratic_residue(10, 13)  # Example check if 10 is quadratic residue mod 13
end = time.time()

print("Is quadratic residue:", result)
print("Execution time:", end - start, "seconds")
