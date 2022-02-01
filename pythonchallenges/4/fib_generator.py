# Generator function is so more efficient

# Generator solution
def fib_generator():
    n = m = c = 1
    while True:
        yield c
        c = m+n
        n = m
        m = c



# Recursive solution
def fib(n):
    if n in (1,2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

