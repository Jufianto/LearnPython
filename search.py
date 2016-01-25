daftar = ['jeruk','mangga','apel']

while True:
    cari = raw_input('Cari BUah : ')
    if not cari:
        print "selesai"
        break
    if cari in daftar:
        print "Ditemukan pada index ke ",
        print 1+ daftar.index(cari)
    else:
        print "tidak ketemu"

