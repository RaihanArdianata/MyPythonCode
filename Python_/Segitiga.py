string = ""

bar = 10

while bar >= 0:
	kol = bar

	while kol > 0:
		string = string + " 2 "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar - 1
	
print (string)