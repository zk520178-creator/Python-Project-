import time

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

start = time.time()
result = mod_inverse(3, 11)
end = time.time()

print("Modular Inverse:", result)
print("Execution Time:", end - start, "seconds")
