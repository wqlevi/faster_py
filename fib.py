def fib(n):
    a = 0.0
    b = 1.0
    for i in range(n):
        tmp = a
        a += b
        b = tmp
    return a


if __name__ == "__main__":
    n = 1000
    res = fib(n)
    print("\nfib of %d is %f" % (n, res))
