import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error:
	print('ERROR: Socket could not be created.')
	sys.exit()
