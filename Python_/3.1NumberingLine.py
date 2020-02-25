name=input("Masukkan Nama File : ")
baris=0
with open(name,'r') as f:
    for line in f:
        baris +=1
        print(baris,line)
#count = 0

#openfile = open("biodata.txt", "r+")

#for lines in openfile:
    #linenumbers = openfile.write(str(count)+'\t'+lines)
    #count += 2


#print(count)