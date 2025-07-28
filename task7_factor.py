import math

def modular_pow(base, exponent, mod):
    """Efficient modular exponentiation: (base^exponent) % mod"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result

def miller_rabin_test_with_factor(p, a):
    """Miller-Rabin test that also prints a factor if p is composite"""
    if p == 2 or p == 3:
        return True, None
    if p <= 1 or p % 2 == 0:
        return False, 2  # even number ⇒ divisible by 2

    # Step 1: write p-1 = 2^b * m
    m = p - 1
    b = 0
    while m % 2 == 0:
        m //= 2
        b += 1

    # Step 2: compute z = a^m mod p
    z = modular_pow(a, m, p)
    if z == 1 or z == p - 1:
        return True, None

    for j in range(b - 1):
        z_prev = z
        z = modular_pow(z, 2, p)

        if z == p - 1:
            return True, None
        if z == 1:
            # Found non-trivial square root of 1: factor
            factor = math.gcd(z_prev - 1, p)
            if 1 < factor < p:
                return False, factor
            else:
                return False, None

    # Final fallback, try gcd(z - 1, p)
    factor = math.gcd(z - 1, p)
    if 1 < factor < p:
        return False, factor

    return False, None

# Take input from user
try:
    p = int(input("Enter the number to test (p): "))
    a = int(input("Enter the base (a): "))

    is_prime, factor = miller_rabin_test_with_factor(p, a)
    if is_prime:
        print(f"{p} may be prime (passed Miller-Rabin test with base {a})")
    else:
        print(f"{p} is composite (failed Miller-Rabin test with base {a})")
        if factor:
            print(f"One non-trivial factor (producer) of {p} is: {factor}")
        else:
            print("Failed to find a factor during the test.")
except ValueError:
    print("Invalid input! Please enter integers only.")
