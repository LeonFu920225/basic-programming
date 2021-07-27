n=int(input("請輸入起始n值:"))
m=int(input("請輸入結束m值:"))
d=int(input("請輸入公差d值:"))
sum=0
if m>n:
    if d>0:
        for num in range(n,m+1,d):
            sum+=num
        print("sum=",sum)
    else:print("遞增時d不可<0!")
elif m==n:
    print(m)
else:
    if d<0:
        for num in range(n,m,d):
            sum+=num
        print("sum=",sum)
    else:print("遞減時d不可>0!")