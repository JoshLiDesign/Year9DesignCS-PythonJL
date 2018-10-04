import os
#A loop structure is a structure that allows us to run a section
#of code a number of times. It is great for when we need to repeat process.
#It is also great when we need to run a pattern.

#There are two broad categories of loops
# Conditional Loop: This loops as long as something is true
# Counted Loop: This loops a set number of times

print("0")
print("1")
print("2")
print("3")
print("4")
print("5")

print("*********************************")

#The general structure of a counted loop is
#count: This is the variable we use to track the number of times a loop runs
#Check: This is the boolean (T or F) statement we evaluate to decide if we keep going
#Change: This is the change in the count that happens after each loop

#We use a for i in a range loop
for i in range(0, 6, 1):
	print(i)

print("*********************************")

#How would the above loop run
# i = 0, 0 < 6, True RUN LOOP
# ...
# i = 6; 6 </ 6, False EXIT LOOP

#os.system("say WHERE THE LOOPS MY BROTHA")

for i in range(7, 105, 1):
	print(i)

print("*********************************")

for i in range(-22, 135, 2):
	print(i)

print("*********************************")

for i in range(3, 0, -1):
	print(i)

for i in range(101, -1, -1):
	print(i)

s = "Fish food"

print("*********************************")

for i in range(0, len(s), 1):
	print(s[i])

print("*********************************")

for i in range(0, len(s), 2):
	print(s[i])
for i in range(len(s)-1, -1, -1):
	print(s[i])