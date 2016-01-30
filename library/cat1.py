import sys

filename = sys.argw[1]
f = open(filename)
print f.read()
f.close()

