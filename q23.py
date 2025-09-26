# 23.Wap to check the given points are lying in which quadrant.

print("1st quardrant" if ((x := int(input("Please enter the value for x axis: ")))>0 and (y := int(input("Please enter the value for y axis: "))))>0 else "2nd quadrant" if x<0 and y>0 else "3rd quardrant" if x<0 and y<0 else "4th quardrant" if x>0 and y<0 else "origin")

del x,y