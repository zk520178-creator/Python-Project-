import time
def pali(n):
    rev = 0
    z = n
    while(z>0):
        rev = rev * 10 + z % 10
        z = z // 10

    if (rev == n):
        print("Palidrome number ")
    else:
        print("Not Palidrome number ")

n = int(input("Enter a number to check: "))
pali(n)

start = time.time()   # start time
pali(n)
end = time.time()     # end time

print("Execution Time:", end - start, "seconds")

# time complexity = O(logn)