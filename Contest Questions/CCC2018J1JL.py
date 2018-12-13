
isSpam = False;
first = int(input());
second = int(input());
third = int(input());
last = int(input());

#print(first+" "+second+" "+third+" "+last);
if first == 8 or first == 9:
	if second == third:
		if last == 8 or last == 9:
			isSpam = True;

if isSpam:
	print("ignore");
else:
	print("answer");