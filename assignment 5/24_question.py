import time

def order_mod(a, n):
    a = a % n
    if a == 0:
        return None
    k = 1
    current = a
    while current != 1:
        current = (current * a) % n
        k += 1
        if k > n:
            return None
    return k

start = time.time()
result = order_mod(3, 7)
end = time.time()

print("Order:", result)
print("Execution time:", end - start, "seconds")
