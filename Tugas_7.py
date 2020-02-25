def hurufDalamNama():
    huruf = {}
    for h in nama:
        jml = 0
        if h in huruf:
            jml = huruf[h]+1
        else:
            jml = 1
        huruf.update({h:jml})
    return  huruf
nama = input("Nama Anda:")
print((hurufDalamNama()))