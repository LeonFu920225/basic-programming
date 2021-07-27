print("The distance between Moon and Earth is 384400km")
x=eval(input("Please enter the rocket speed(mach):"))
y=1225*x
time=(384400/y)
total_days=time//24
total_hours=time%24
total_minutes=(total_hours%1)*60
toal_seconds=(total_minutes%1)*60
print("It takes {:^2.0f} days and {:^2.0f} hours and {:^2.0f} minutes and {:^2.0f} seconds"
      " for the rocket to fly from the Earth to the Moon".
      format(total_days,total_hours,total_minutes,toal_seconds))