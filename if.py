nama=raw_input('Nama : ')
Alamat=raw_input ('Alamat : ')
hobi = raw_input('Hobi ')

print "nama ",nama
print 'Alamat ' ,Alamat
while not hobi:
    if hobi:
        print 'hobi ',hobi
    else:
        print "sebaiknya hobi anda Di Isi"
        hobi = raw_input('hobi')
