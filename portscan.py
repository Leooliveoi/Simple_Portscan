# -*- coding: utf-8 -*-
'''Criando Portscan com Python'''
''' Lang = Pt-BR '''

import socket
import sys


def scan(host, port, timeout = 0.5):
	#Retorna um status code

	print(host)
	for port in ports:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(float(timeout))
		code = client.connect_ex((host,int(port)))
		if code == 0:
			print("[+]{} Open".format(port))
		else:
			print("[-]{} Closed".format(port))
			




if __name__ == "__main__":
	timeout = 0.5
	ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]
	host = "google.com"
	if len(sys.argv) >= 2:
		# Indice 0 se refere ao proprio nome do arquivo no array sys.argv
		host = sys.argv[1]
		if len(sys.argv) >= 3:
			ports = sys.argv[2].split(",")
			if len(sys.argv) >= 4:
				timeout = sys.argv[3]
		else:
			ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]
		scan(host, ports, timeout=timeout)
	else:
		print("Usage portscan.py {} {} with {}s".format(host, ports, timeout))
		scan(host, ports, timeout)



 







