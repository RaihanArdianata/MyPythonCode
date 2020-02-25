#def menu():
print('=============================')
print('MENU PILIHAN')
print('1.Konversi Uang DOLLAR ke RUPIAH')
print('2.Konversi Uang RUPIAH ke DOLLAR')
print('3.Keluar')
print('=============================')
a=(int(input('Masukkan Pilihan:' )))
kurs=(float(14757.30))

if a == 1:
    usd = (int(input('Masukkan Jumlah USD = $ ')))
    hitung=(float(usd*kurs))
    print('Kurs Rupiah Sekarang = %.6f'%(kurs))
    print('Nilai USD $ %.6f = Rp %.6f'%(usd,hitung))
elif a== 2:
    idr = (int(input('Masukkan Jumlah IDR = Rp ')))
    hitung = (float(idr / kurs))
    print('Kurs Rupiah Sekarang = %.6f' % (kurs))
    print('Nilai IDR Rp %.6f = $ %.6f' % (idr, hitung))

elif a== 3:
    exit()
else :
    print("Perintah Salah")
    #menu()
#if __name__ == "__main__":

    #menu()