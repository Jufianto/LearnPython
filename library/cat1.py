import sys

if not sys.argv[1:]: # 1: berfungsi untuk pemengalan list (see pmllist)
    print ('Cara menggunakannya adalah %s <nama-file>' % sys.argv[0])
    sys.exit()

filename = sys.argv[1]
f = open(filename)
print f.read()
f.close()


