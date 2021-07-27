feet=int(input("請輸入腳的數量:"))
number=int((input("請輸入一共有幾隻雞和兔子:")))
chicken=0
while 0<number<feet and 4*number>feet:
    rabbit=number-chicken
    if 2*chicken+4*rabbit==feet:
        print("雞有{}隻，兔有{}隻".format(chicken,rabbit))
        break
    chicken+=1
else:
    print("無解!")