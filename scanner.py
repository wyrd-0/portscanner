from scapy.all import sr1,IP,TCP
import sys

if len(sys.argv) < 2:
	print("Usage: scanner.py REMOTE_IP")
	sys.exit(1)

target = sys.argv[1]

res, unans = sr( IP(dst=target) /TCP(flags="S", dport=(1,1024)) )

res.nsummary( lfilter=lambda (s,r): (r.hashlayer(TCP) and (r.getlayer(TCP).flags & 2)) )
