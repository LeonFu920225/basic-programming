num = eval(input("請輸入共要多少個質數:"))
prime = []
count = 0
for i in range(2, 1000000):
    if i == 2:
        prime.append(i)
    else:
        for n in range(2, i-1):
            if i % n == 0:
                break
        else:
            prime.append(i)
            count += 1
    if count == num:
        break
print(prime)