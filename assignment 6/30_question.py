import time

def is_carmichael(n):
    start = time.time()
    if n < 3:
        print("Execution Time:", time.time() - start, "seconds")
        return False

    for a in range(2, n):
        if n % a != 0:  # only check numbers coprime to n (roughly)
            if pow(a, n - 1, n) != 1:
                print("Execution Time:", time.time() - start, "seconds")
                return False

    print("Execution Time:", time.time() - start, "seconds")
    return True

# Example
n = int(input("Enter a number: "))
if is_carmichael(n):
    print(n, "is a Carmichael Number.")
else:
    print(n, "is NOT a Carmichael Number.")
