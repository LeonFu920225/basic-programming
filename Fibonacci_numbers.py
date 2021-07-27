def fib(n):
    if n == 0 or n == 1:
        return n
    a,b = 0,1
    for i in range(2, n+1):
        temp = b
        b = a+b
        a = temp
    return b
n = eval(input("Please enter a number(>=2):"))
for i in range(0,n):
    print("fib({}) = {}".format(i, fib(i)))