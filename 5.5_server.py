import socket
import tqdm
import os

host = ''
port = 8888
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
try:
	s.bind((host, port))
except socket_error as e:
	print(str(e))

print(f"[*] Listening as {host}:{port}")
s.listen(5)

ClientSocket, addr = s.accept()
print(f"[+] {addr} is connected.")

received = ClientSocket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

#remove absolute path if there is
filename = os.path.basename(filename)

#convert to integer
filesize = int(filesize)

#start receiving file from the socket
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit = "B", unit_scale = True, unit_divisor = 1024)

with open(filename, "wb") as f:
	while True:
		bytes_read = ClientSocket.recv(BUFFER_SIZE)
		if not bytes_read:
			#file transmitting is done
			break

		#write the received bytes to the file
		f.write(bytes_read)

		#update the progress bar
		progress.update(len(bytes_read))

ClientSocket.close()
s.close()
