def fibonacci(n):
    fib=[0,1]
    for i in range(2,n):
        fib_series=fib[-1]+fib[-2]
        fib.append(fib_series)
    return fib
n=int(input())
print(fibonacci(n))
