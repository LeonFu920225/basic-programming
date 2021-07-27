list = []
while True:
    number = input("Please enter the number(Q or q to quit):")
    if number == 'Q' or number == 'q':
        break
    else:
        list.append(eval(number))
print("The original list:", list)

def bubble_sort(list):
    length = len(list)
    for i in range(length-1):
        for j in range(length-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print("The sorted list:", bubble_sort(list))