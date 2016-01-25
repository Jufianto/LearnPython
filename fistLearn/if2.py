lanjut = 'Y'
while lanjut != 'S':
    nama=raw_input('Nama : ')
    if not nama:
        print 'nama harus Diisi'
        continue
    alamat= raw_input('Alamat : ')
    if not alamat:
        print 'Alamat Harus Di Isi '
        continue
    hobi= raw_input('Hobi : ')
    if not hobi:
        print 'Hobbi Harus Di isi '
        continue
    print "------------------------------------------"
    print 'Nama : ',nama
    print 'Alamat : ',alamat
    if hobi:
        print ' Hobi : ',hobi
    else:
        print 'Sebaiknya hobi diisi'
    lanjut = raw_input('Tekan "S" jika Selesai').upper()


