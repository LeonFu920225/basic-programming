money=eval(input("請輸入本金:"))
rate=eval(input("請輸入年利率(%):"))
years=eval(input("請輸入年數:"))
for i in range(years):
    money*=(1+rate)
    print("第{}年的本金和{}".format(i+1,int(money)))