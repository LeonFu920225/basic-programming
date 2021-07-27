import math
dir(math)
r=6371
x1=eval(input("請輸入第一個地點緯度:"))
y1=eval(input("請輸入第一個地點經度:"))
x2=eval(input("請輸入第二個地點緯度:"))
y2=eval(input("請輸入第二個地點經度:"))
d=6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))
  +math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1-y2)))
print("distance={:5.1f}""km".format(d))