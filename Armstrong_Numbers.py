start, end = eval(input("Please enter the range of armstrong number <= 3 digit(x,y):"))
list = []
while True:
    if (int(start/100)<1 or int(start/100) > 10) or (int(end/100)<1 or int(end/100) >= 10):
        print("Out of range!")
        break
    for i in range(start, end+1):
        a = int(i/100)
        b = int((i%100)/10)
        c = int(i%10)
        if a**3 + b**3 + c**3 == i:
            list.append(i)
    if list == [] or list == [1]:
        print("None!")
    else:
        for i in range(len(list)):
            print(list[i])
    break