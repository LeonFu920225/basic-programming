a,b,c=eval(input("Please enter the coefficient of the equation:"))
r1=(-b+b**2-4*a*c)/(2*a)
r2=(-b-b**2-4*a*c)/(2*a)
if (b**2-4*a*c)>0:
    print("This equation has two real root.")
    print("r1=%6.2f,    r2=%6.2f"%(r1,r2))
elif (b**2-4*a*c)==0:
    print("This equation has one repeated real root.")
    print("r1=%6.2f" % (r1))
else:
    print("This equation has no real root.")