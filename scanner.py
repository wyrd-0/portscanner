import socket
import sys

if len(sys.argv) < 2: print("Usage: scanner.py REMOTE_IP")

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error:
	print('ERROR: Socket could not be created.')
	sys.exit()
