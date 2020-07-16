x=input()
if len(x)==10 and int(x[0]) in [7,8,9] and sorted(x)[-1].isnumeric():
	print("Valid")
else:
	print("Invalid")