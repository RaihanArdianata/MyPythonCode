print("Hello")

a = 3
b = 2
if a>b:
	print("3>2 bro")
else :
	print("salah")

x = "Raihan Ardi" # x is now of type str
print(x)

x = 5
y = 10
print(x + y)

x = "Hi Dude"
print (x + "Hello")

x = 1
y = 1.2
z = 1j
print(type(x))
print(type(y))
print(type(z))

x = str("Hello")
y = int(1)
z = float(3.4)
print(type(x))
print(type(y))
print(type(z))

b = "Raihan Ardianata"
print(b[0:7])

a = " Raihan Ardianata "
print(a.strip())
print(a) 

a = "Aihan"
print(a.replace("A", "J"))

a = "Raihan, Ardianata,Jihan"
print(a.split(","))

jurusan = ["RPL","TKJ","TJA"]
for a in jurusan:
	print(a)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")#memasukkan
print(thislist)

thislist = ["TJA","RPL","TKJ"]#list
thislist.append("FARMASI") #menambah
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()#mirip remove() tapi menghilangkan di akhir
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]##mirip remove() dan pop index spesifik
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("banana" in thislist)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

i = 1
while i < 6:
  print(i)
  i += 1
  
for x in range(2, 30, 3):
  print(x)