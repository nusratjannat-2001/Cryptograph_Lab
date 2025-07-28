def modular_pow(base, exponent, mod):
    """Efficient modular exponentiation: (base^exponent) % mod"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result = (result * base) % mod
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % mod
    return result

def miller_rabin_test(p, a):
    """Performs the Miller-Rabin test for a given base a"""
    if p == 2 or p == 3:
        return True
    if p <= 1 or p % 2 == 0:
        return False

    # Write p-1 as 2^b * m
    m = p - 1
    b = 0
    while m % 2 == 0:
        m //= 2
        b += 1

    # Compute z = a^m mod p
    z = modular_pow(a, m, p)
    if z == 1 or z == p - 1:
        return True

    for j in range(b - 1):
        z = modular_pow(z, 2, p)
        if z == p - 1:
            return True
        if z == 1:
            return False

    return False

# Take input from user
try:
    p = int(input("Enter the number to test (p): "))
    a = int(input("Enter the base (a): "))

    if miller_rabin_test(p, a):
        print(f"{p} may be prime (passed Miller-Rabin test with base {a})")
    else:
        print(f"{p} is composite (failed Miller-Rabin test with base {a})")
except ValueError:
    print("Invalid input! Please enter integers only.")
