def myPow(x, n):
    # Handle negative powers
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    while n > 0:
        # If n is odd, multiply result by x
        if n % 2 == 1:
            result *= x

        # Square the base
        x *= x
        # Divide n by 2
        n //= 2

    return result


# ---- Main Program ----
if __name__ == "__main__":
    x = float(input("Enter value of x: "))
    n = int(input("Enter value of n: "))

    answer = myPow(x, n)
    print("Result:", answer)

