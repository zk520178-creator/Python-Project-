import time

def crt(remainders, moduli):
    start = time.time()
    M = 1
    for m in moduli:
        M *= m  # multiply all moduli

    x = 0
    for i in range(len(remainders)):
        Mi = M // moduli[i]  # partial product
        # find modular inverse of Mi mod moduli[i]
        for inv in range(1, moduli[i]):
            if (Mi * inv) % moduli[i] == 1:
                break
        x += remainders[i] * Mi * inv

    result = x % M
    end = time.time()
    print("Execution time:", end - start, "seconds")
    return result

# Example
remainders = [2, 3, 2]
moduli = [3, 5, 7]

ans = crt(remainders, moduli)
print("The solution x is:", ans)
