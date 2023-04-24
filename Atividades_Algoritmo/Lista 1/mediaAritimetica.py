# Programa para a media aritimetica de numeros;
import sys
sys.argv.pop(0)
n1, n2, n3 = map(int,sys.argv)

print((n1+n2+n3)/len(sys.argv))