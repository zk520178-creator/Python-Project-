import time

def polygonal_number(s, n):
    start = time.time()
    num = ((s - 2) * n * n - (s - 4) * n) // 2
    end = time.time()
    print("Execution Time:", end - start, "seconds")
    return num

# Example
s = int(input("Enter sides (s): "))
n = int(input("Enter term (n): "))
print("Polygonal Number:", polygonal_number(s, n))
