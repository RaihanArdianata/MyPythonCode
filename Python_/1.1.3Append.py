nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
teks = "Nama: {}\nUmur: {}\nAlamat: {}\n".format(nama, umur, alamat)
file = open("biodata.txt", "a")
file.write(teks)
file.close()
