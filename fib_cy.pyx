def fib_cy(int n):
    cdef double a = 0.0, b=1.0
    cdef int i
    for i in range(n):
        a,b = a+b,a
    return a
