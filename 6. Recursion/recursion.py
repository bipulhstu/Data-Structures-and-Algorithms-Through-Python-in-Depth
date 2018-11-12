def fact(n):
    # assuming that n is a positive integer or 0
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

print("0! =", fact(0))
print("1! =", fact(1))
print("2! =", fact(2))
print("3! =", fact(3))
print("4! =", fact(4))


def fib(n):
    # assuming that n is a positive integer
    if n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1

print("fib(1) =", fib(1))
print("fib(2) =", fib(2))
print("fib(3) =", fib(3))
print("fib(4) =", fib(4))
print("fib(5) =", fib(5))
