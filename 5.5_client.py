import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = '192.168.56.101'
port = 8888

filename = input('Enter the name of file to send: ')
filesize = os.path.getsize(filename)

s = socket.socket()

print(f'[+] Connecting to {host}:{port}')
s.connect((host, port))
print("[+] Connected")

s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#send the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit = 'B', unit_scale = True, unit_divisor = 1024)

with open(filename, "rb") as f:
	while True:
		#read bytes from file
		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			#file transmitting is done
			break

		s.send(bytes_read)

		#update the progress bar
		progress.update(len(bytes_read))

s.close()
