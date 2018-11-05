#This program takes in two floats and calculates 
#the fluctuation rate, rounded to 2 decimals


#input - takes in two doubles
n = float(input("enter num 1: "))
m = float(input("enter num 2: "))

diff = m/n
diff = diff*100
diff = diff-100

if diff > 0:
	print("+" + "%.2f" % diff + "%");
else:
	print("%.2f" % diff + "%")