import random
money = 300
bet = 100
min,max = 1,100
winpercent = int(input("請輸入莊家贏的比率(0~100):"))

while True:
    print("Welcome!, Now you have %d dollars" % money)
    print("You can bet %d dollars every time" % bet)
    print("Guess big or small:l or L mean big, S or s mean small, Q or q to quit")
    customernum = input("= ")
    if customernum == 'Q' or customernum == 'q':
        break
    num = random.randint(min,max)
    if num > winpercent:
        print("Right!")
        money += bet
    else:
        print("Wrong!")
        money -= bet
    if money <= 0:
        break
print("Game over!")