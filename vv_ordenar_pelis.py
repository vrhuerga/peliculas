#!/usr/bin/python
import sys
import os
from os import listdir

if len(sys.argv) == 1:
	print "se necesita un argumento"
	exit()

ruta=sys.argv[1]

#Calse que no uso por ahora pero sirve de prueba :-)
class C_ManejoFicheros():
	x_ruta = ""
	def imprimir(self):
		print x_ruta 

O_pelis = C_ManejoFicheros()
O_pelis.x_ruta = ruta
print O_pelis.x_ruta


for fichero in listdir(ruta):
	os.system('clear')
	print fichero	
#	os.system('mplayer '+"'"+ruta+fichero+"'")
	print "'B' Borrar, 'C' Copiar"
	comando = raw_input()
	if comando == "B" or comando == "b":
		print "BORRANDO"	
		os.system('rm '+"'"+ruta+fichero+"'")
	elif comando== "C" or comando == "c":
		print "COPIANDO"
	else:
		print "NO HACER NADA"

