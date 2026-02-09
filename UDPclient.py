import socket 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
except socket.error: 
    print("Cannot create socket")
    exit()

while True:
    try:
        m = input("Message to server: ")
        s.sendto(bytearray(m, encoding="ascii"), ("192.168.73.235", 44444))
        try:
            m, addr = s.recvfrom(1000)
            print(m.decode("ascii"))
        except (ConnectionResetError, OSError): 
            print("something wrong, quit")
            break 
    except KeyboardInterrupt: break 

s.close()
