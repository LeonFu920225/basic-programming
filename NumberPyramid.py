h=eval(input("Please enter the pyramid's height:"))
for i in range(h):
    for k in range(h-i-1):
        print(' ', end='')
    for j in range(i):
        print(i+1-j, end='')
    for l in range(i + 1):
        print(l + 1, end='')
    print()