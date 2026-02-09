#UDP sequential server program
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
except socket.error:
    print("Cannot create socket")
    exit()

s.bind(('', 44444)) # make a binding, this operation may fail
print("UDP server waiting for clients")
while True:
    try:
        m, caddr = s.recvfrom(1000)
        print(f"[{caddr}]: {m.decode("ascii")}")
        m = input("Msg back to: ")
        s.sendto(bytearray(m, encoding="ascii"), caddr)
        # you can send something back at here
    except socket.error:
        print("recvfrom error")