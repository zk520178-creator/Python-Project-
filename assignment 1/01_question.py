import math
import time

def euler_phi(n):
    count = 0
    for k in range(1, n+1):
        if math.gcd(n, k) == 1:
            count += 1
    return count

n = 9000
start = time.time()
result = euler_phi(n)
end = time.time()

print("Euler's Totient Function for", n, "is:", result)
print("Execution time: {:.8f} seconds".format(end - start))



# the time complexity is = O(nlogn)


