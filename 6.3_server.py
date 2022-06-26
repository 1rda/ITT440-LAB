import socket
import errno
import math
from multiprocessing import Process

host = ''
port = 8888

def process_start(s_sock):
		s_sock.send(str.encode('Welcome to the Server'))

		while True:
			info = s_sock.recv(2048)
			info = info.decode('utf-8')

			try:
				option, num = info.split(" ", 2)
			except:
				print("[!] Data not received")
				break

			if (option == 1):
				answer = math.log(float(num))
				#s_sock.send(str.encode(str(answer)))

			elif (option == 2):
				answer = math.sqrt(float(num))
				#s_sock.send(str.encode(str(answer)))

			elif (option == 3):
				answer = math.exp(flaot(num))
				#s_sock.send(str.encode(str(answer)))

			elif (option == 'exit'):
				break

			result = str(answer)
			s_sock.send(str.encode(result))

		s_sock.close()

if __name__ == '__main__':
	s = socket.socket()
	try:
		s.bind((host, port))
	except socket_error as e:
		print(str(e))

	print(f'[*] Listening on port {port}')
	s.listen(3)

	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				p = Process(target = process_start, args = (s_sock,))
				p.start()
			except socket.error:
				print('Got a socket error')
	except Exception as e:
		print('An exception occured!')
		print(e)
		sys.exit(1)

	finally:
		s.close()
