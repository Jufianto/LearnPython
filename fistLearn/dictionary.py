daftar = {
	2: 'jeruk',
	7: 'Mangga',
	4: 'pisang',
	3: 'jambu',
	9: 'aple' ,

}
print daftar
while True:
	key=raw_input('Kode barang :')

	if not key:
		print 'Selesai'
		break
	key = int(key)
	if key in daftar:
		print daftar[key]
	else:
		print 'Kode Barang ' , key , "tidak ditemukan "