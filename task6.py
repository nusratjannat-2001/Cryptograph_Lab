import random

def lehmann_primality_test(p, t=5):
    """
    Lehmann's probabilistic primality test.
    :param p: Integer to test for primality
    :param t: Number of iterations to repeat
    :return: String result
    """
    if p <= 3:
        return "Prime" if p > 1 else "Not prime"

    for i in range(t):
        a = random.randint(2, p - 2)
        exponent = (p - 1) // 2
        x = pow(a, exponent, p)

        print(f"Test {i+1}: a = {a}, a^((p-1)/2) mod p = {x}")

        if x != 1 and x != p - 1:
            return f"{p} is composite."

    return f"{p} is probably prime with error probability <= 1 in 2^{t}."

if __name__ == "__main__":
    P = int(input("Enter number P: "))
    t = int(input("Enter number of tests t: "))
    result = lehmann_primality_test(P, t)
    print(result)
