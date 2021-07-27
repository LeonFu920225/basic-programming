def functions(x,y):
    addresult = x + y
    subresult = x - y
    mulresult = x * y
    divresult = x / y
    return addresult, subresult, mulresult, divresult
stop = 0

while stop == 0:
    x = int(input("請輸入第一個數字:"))
    y = int( input("請輸入第二個數字:"))
    calculate = input("請輸入運算子(+, -, *, /):")
    add, sub, mul, div = functions(x,y)
    if calculate == '+':
        print("The result is:", add)
    elif calculate == '-':
        print("The result is:", sub)
    elif calculate == '*':
        print("The result is:", mul)
    elif calculate == '/':
        print("The result is:", div)
    else:
        print("運算子格式錯誤!")
    go = str(input("是否繼續?(y or Y = yes):"))
    if go == 'y' or go == 'Y':
        continue
    else:
        stop += 1
        break