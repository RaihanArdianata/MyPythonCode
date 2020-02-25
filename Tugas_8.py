from math import *
while 1:
	r = input("x = ")
	if r == "":
		break
	exec("x = " + r)
	print(x)
	v = x * 3
	print(v)
	v = x + 3
	print(v)
	v = sin(x)
	print(v)
	v = pi * (10 ** 2)
	print(v)