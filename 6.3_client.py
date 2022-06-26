import socket

host = '192.168.56.101'
port = 8888

s = socket.socket()

print('[+] Connecting to host.')
s.connect((host, port))
print('[+] Connected.')

while True:
	print('ONLINE CALCULATOR\n')
	print('1. Logarithmic Calculator')
	print('2. Square Root Calculator')
	print('3. Exponential Calculator')
	print('4. Exit\n')
	option = input('Choose an option: ')

	if (option == 4):
		s.send(str.encode('exit'))
		break

	num = input("Number: ")

	info = option + " " + num
	s.send(str.encode(info))

	answer = s.recv(1024)
	print(answer.decode('utf-8'))

s.close()



