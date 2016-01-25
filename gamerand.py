
import random #import library dari random
list =[1] # variabel berbentuk list , sama seperti array
for x in range(0,10): #perulangan dengan menggunakan range
    dataRange = random.randrange(0,20) #melakukan  random data dari 0 - 20
    list.append(dataRange) #menambahkan data dari list

print "-------------------------------"
print "Program Menebak Angka dari 1 - 20 "
print "syntax '?' untuk bantuan , syntax 'help' for jawaban"
#input = raw_input("Masukan Tebakan Anda : ")
jawaban = str(random.choice(list))
a = ''
while True:
    input = raw_input("Masukkan Tebakan Anda : ") #mendapatkan hasil inputan dari user
    if (input == jawaban):
        print "Selamat Anda Menang"
        break
    elif (input== '?'):
        print "Data kemungkinan anda tebak  adalah ",list
        print "Tapi anda hanya memiliki 3 kesempatan"
        a=1
       # input =raw_input("Masukan Tebakan Anda : ")
        continue
    elif (input.lower() == 'help'):
        print "Anda Kalah Jawabannya adalah ", jawaban
        break
    else:
       # input =raw_input("Masukan Tebakan Anda : ")
        if a:
            a=a+1
            print "Anda memiliki %s kesempatan" %(4-a)
            if (a==4):
                print "anda kalah , Jawabannya adalah " , jawaban
                break
        #input = raw_input("Masukan Tebakan Anda : ")
        continue



