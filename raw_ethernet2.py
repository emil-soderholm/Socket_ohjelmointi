import socket as sc
import struct

# Constants for clarity
DEST_MAC = b'\xaa\xbb\xcc\xdd\xee\xff'
SRC_MAC = b'\x00\x01\x02\x03\x04\x05'
ETHER_TYPE = b'\x08\x00' # IPv4

header = struct.pack("!6s6s2s", DEST_MAC, SRC_MAC, ETHER_TYPE)
payload = b"CHRYSLER!!! TOIMISKO TAA HALOO HALOO"
packet = header + payload

# Note: You'll likely need to run this with sudo
try:
    rs = sc.socket(sc.PF_PACKET, sc.SOCK_RAW, sc.htons(0x0800))
    rs.bind(("enp0s3", 0))
    rs.send(packet)
    print("Packet sent successfully!")
except PermissionError:
    print("Error: You need root privileges to run raw sockets.")
except Exception as e:
    print(f"An error occurred: {e}")