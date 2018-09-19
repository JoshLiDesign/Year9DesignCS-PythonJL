print("Slope Calculator:")

#Input
x1 = input("Input x1: ")
x1 = int(x1);
y1 = input("Input y1: ")
y1 = int(y1);

x2 = input("Input x2: ")
x2 = int(x2);
y2 = input("Input y2: ")
y2 = int(y2);

#Process
rise = x2 - x1
run = y2 - y1;
fSlope = rise/run;

#String stores chars
#int stores integer values
#floats tores real numbers

#Output
print(rise)
print(run)
print("your slope is m = "+str(rise)+"/"+str(run))
print("your slope as a decimal is "+str(rise/run))