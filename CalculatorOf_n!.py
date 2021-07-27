def factorial(n):
    if n == 1:
        return 1
    elif n != int:
        print("Error!")
    else:
        return (n*factorial(n-1))
N = eval(input("Please enter a number:"))
print(N, "'s factorial result = ", factorial(N))