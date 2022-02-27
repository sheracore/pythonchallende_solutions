# Recursive solution
def fib_recursive(n):
    print(n)
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursive(n-1) + fib_recursive(n-2)
    return result

# Memoized solution
def fib(n, memo):
    print(n, memo)
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return result

def fib_dp_up_bottom(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


# Buttom_up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    
    for i in range(3, n+1):
        print(bottom_up)
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


print(fib_recursive(11))
print(fib_dp_up_bottom(11))
print(fib_bottom_up(11))